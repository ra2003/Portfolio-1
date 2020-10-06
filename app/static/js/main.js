var isInViewport = function (elem) {
    var bounding = elem.getBoundingClientRect();
    return (
        bounding.top >= 0 &&
        bounding.left >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
};

let headshot = document.getElementById('headshot');
let footer = document.getElementById('footer');
window.addEventListener('scroll', function (e){
    if (!isInViewport(headshot)) {
        footer.classList.remove('d-none');
    } else {
        footer.classList.add('d-none');
    }
});