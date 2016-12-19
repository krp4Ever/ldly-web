$(function () {
    $('.unslider').hover(function (){
        $('.unslider-active  .slider-item-desc').stop()
        $('.unslider-active  .slider-item-desc').fadeIn()

    },
    function() {
        $('.unslider-active  .slider-item-desc').stop()
        $('.unslider-active  .slider-item-desc').fadeOut()
    })
})
