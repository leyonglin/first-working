function getXhr(){
    if(window.XMLHttpRequest){ 
        return new XMLHttpRequest();              
    }else{
        return new  ActiveXObject("Microsoft.XMLHTTP")
    }
}

function createXhr(){
	var xhr=null;
	if(window.XMLHttpRequest){
		xhr = new XMLHttpRequest();
	}else{
		xhr = new ActiveXObject("Microsoft.XMLHTTP");
	}
	return xhr;
}


<script src="/static/js/jquery-1.11.3.js"></script>
{% block js %}
	<script>
		$(function(){
			$("#btnRegister").click(function(){
				location.href='/register';
			});
		});
	</script>