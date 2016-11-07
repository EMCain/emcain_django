/**
 * Created by Emily on 11/7/2016.
 */

function toggleNav(){
    var x = document.getElementsByClassName('top-navbar')[0];
    if (x.className === 'top-navbar') {
        x.className += ' responsive';
    } else {
        x.className = 'top-navbar';
    }
}