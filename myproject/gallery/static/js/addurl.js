$("#id_qiniu_url").focus(function(){
  console.log('hahahahahahaha');
  var get_url = $(".info").find("a").attr("href");
  console.log(get_url);
  $(this).attr('value',get_url);
});
