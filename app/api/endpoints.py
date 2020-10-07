from flask import request
from flask_restx import Resource
from app import restx
from . import api
from resume import Resume

resume = Resume()

resume_api = restx.namespace(
    "resume", description="Get info about me through the rest API"
)

testing_api = restx.namespace("test", description="API routes for testing")


# This gets overwritten by rest-x
@api.route("/", methods=["GET"])
def root():
    return ""


# RESUME API
@resume_api.route("/get_all")
@resume_api.doc(
    description="Get my whole resume as json", responses={200: "(json map) My resume"}
)
class GetAll(Resource):
    def get(self):
        return {
            "info": resume.info,
            "skills": resume.skills,
            "education": resume.education,
            "experience": resume.experience,
            "projects": resume.projects,
            "hobbies": resume.hobbies,
            "pitch": resume.pitch,
            "references": resume.references,
        }


@resume_api.route("/info")
@resume_api.doc(
    description="Get my contact info", responses={200: "(json map) My contact info"}
)
class GetInfo(Resource):
    def get(self):
        return resume.info


@resume_api.route("/skills")
@resume_api.doc(description="Get my skills", responses={200: "(json list) My skills"})
class GetSkills(Resource):
    def get(self):
        return resume.skills


@resume_api.route("/education")
@resume_api.doc(
    description="Get my education", responses={200: "(json list) My education"}
)
class GetEducation(Resource):
    def get(self):
        return resume.education


@resume_api.route("/experience")
@resume_api.doc(
    description="Get my experience", responses={200: "(json list) My experience"}
)
class GetExperience(Resource):
    def get(self):
        return resume.experience


@resume_api.route("/projects")
@resume_api.doc(
    description="Get my projects", responses={200: "(json list) My projects"}
)
class GetProjects(Resource):
    def get(self):
        return resume.projects


@resume_api.route("/hobbies")
@resume_api.doc(description="Get my hobbies", responses={200: "(json list) My hobbies"})
class GetHobbies(Resource):
    def get(self):
        return resume.hobbies


@resume_api.route("/pitch")
@resume_api.doc(description="Get my pitch", responses={200: "(string) My pitch"})
class GetPitch(Resource):
    def get(self):
        return resume.pitch


@resume_api.route("/references")
@resume_api.doc(
    description="Get my references", responses={200: "(json list) My references"}
)
class GetReferences(Resource):
    def get(self):
        return resume.references


# TESTING ROUTES
@testing_api.route("/get_test")
@testing_api.doc(
    description="Test a get request (with optional query param)",
    params={"test_query": "Optionally pass in a test query"},
)
class GetTest(Resource):
    def get(self):
        return {"hello": "world", "query": request.args.get("test_query", "")}


@testing_api.route("/post_test")
@testing_api.doc(
    description="Test posting to the server. It can accept any number of form params.",
    params={
        "field1": "Test text to post",
        "field2": "Test text to post",
        "field3": "Test text to post",
    },
)
class PostTest(Resource):
    def post(self):
        form = [{"name": name, "value": value} for name, value in request.args.items()]
        return {"Form": form}
