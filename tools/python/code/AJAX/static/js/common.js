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