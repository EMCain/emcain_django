/**
 * Created by Emily on 11/7/2016.
 */
function toggleSkillShow(event) {
    var titleDiv = event.currentTarget;
    var info = titleDiv.parentNode.getElementsByClassName('skill-info')[0];
    if (info.className === 'skill-info') {
        info.className += ' show';
        titleDiv.querySelector('span').innerHTML = ' &#45; ';
    } else {
        info.className = 'skill-info';
        titleDiv.querySelector('span').innerHTML = '&#43; ';
    }
}

window.onload = function(){
    var names = document.getElementsByClassName('skill-name');

    for (var i = 0; i < names.length; i++) {
        names[i].addEventListener('click', toggleSkillShow, false);
    }
};