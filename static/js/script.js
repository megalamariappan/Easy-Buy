setTimeout(function(){
    alerts=document.getElementsByClassName('alert');
    for(let i=0;i<alerts.length;i++){
        alerts[i].style.display="none";
    }
},2000)