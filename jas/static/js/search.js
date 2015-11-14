//$(document).ready(function(){
//	$("#search-box").keyup(function(){
//		$.ajax({
//		type: "POST",
//		url: "search",
//		data:'keyword='+$(this).val(),
//		beforeSend: function(){
//			$("#search-box").css("background","#FFF url(LoaderIcon.gif) no-repeat 165px");
//		},
//		success: function(data){
//			$("#suggesstion-box").show();
//			$("#suggesstion-box").html(data);
//			$("#search-box").css("background","#FFF");
//		}
//		});
//	});
//});
////To select country name
//function selectCountry(val) {
//$("#search-box").val(val);
//$("#suggesstion-box").hide();
//}
//
//$('#search').autocomplete({
//
//    source: function(request, response){
//        $.ajax({
//
//            type: 'GET',
//			cache   : false,
//            dataType: 'json',
//            serviceUrl : '/search/',
//            data:{
//                //maxRows: 12, // показать первые 12 результатов
//                query: $(this).val() // поисковая фраза
//
//            },
//
//            //success: function(data){
//            //    response($.map(data, function(item){
//            //        return {
//            //            plink: item.plink, // ссылка на страницу товара
//            //            label: item.title_ru // наименование товара
//            //        }
//            //    }));
//            //}
//        });
//    },
//    //select: function( event, ui ) {
//    //    // по выбору - перейти на страницу товара
//    //    // Вы можете делать вывод результата на экран
//    //    location.href = ui.item.plink;
//    //    return false;
//    //}
//    //minLength: 3 // начинать поиск с трех символов
//});
$(function() {
  $("#autocomplete").autocomplete({
     source: function(request, response) {
        $.get('/search/', { query: request.term },
			function(data) {
           response($.map(JSON.parse(data.split('\n')), function (value, key) {

           return {
                    label: value['title'],
                    value: key,
                    url: value['url'],
                    price: value['price']
                };

      }));
        }) },
      select: function( event, ui ) {
        // по выбору - перейти на страницу товара
        // Вы можете делать вывод результата на экран
          console.log(event)
          console.log(ui.item.url)
        location.href = ui.item.url
        return false;
    },
    minLength: 2,
  });
});