console.log("javascript start")
  
$(document).ready(function() {
    $('.fadein-left').waypoint(function(direction) {
        $('.fadein-left').addClass('fadein')
          
    },{
        offset:'500px'
    })

    $('.fadein-right').waypoint(function(direction) {
        $('.fadein-right').addClass('fadeinRight')
          
    },{
        offset:'500px'
    })

    $('.freelancer-section').waypoint(function(direction) {
        $('.freelancer-section').addClass('myfadeIn')
          
    },{
        offset:'500px'
    })

    $('.service-card-bounce').waypoint(function(direction) {
        $('.service-card-bounce').addClass('bounce-out')
          
    },{
        offset:'500px'
    })

    $('.work-card-animate').waypoint(function(direction) {
        $('.work-card-animate').addClass('animate__zoomin')
          
    },{
        offset:'600px'
    })

})