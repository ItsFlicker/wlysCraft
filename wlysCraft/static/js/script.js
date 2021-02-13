$(document).ready(function(){
    $(function(){
        var $main = $('#main')
        $main.hide().fadeIn(800)
        $('.btn').click(function(){
            $('.progress').css('display', 'inline')
        })
    });

    function activeM(){
        $('.sidenav').sidenav();
        $('input#LoginUsername, input#RegisterUsername').characterCounter();
    }

    activeM()
});