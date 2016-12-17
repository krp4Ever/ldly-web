$(".tab-box .tab-nav >a").click(
   function(){
       $(this).addClass("cur").siblings().removeClass("cur");
       $(".tab-box .tab-content ul").eq($(this).index()).show().siblings().hide();
   }
);
