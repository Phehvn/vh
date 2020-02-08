
$(document).ready(function() {
	// back to top
    var topBtn = $('.back-to-top');
	topBtn.hide();
	$(window).scroll(function () {
		if ($(this).scrollTop() > 0) {
			topBtn.fadeIn();
			$('#header').addClass('fixed');
		} else {
			topBtn.fadeOut();
			$('#header').removeClass('fixed');
		}
	});
	topBtn.click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 500);
		return false;
	}); // end back to top
	// slider
	$('.slideshow').not('.slick-initialized').slick({
		arrows: false,
		slidesToShow: 1,
		slidesToScroll: 1,
		infinite: true,
		autoplay: true,
		dots:true,
		autoplaySpeed: 10000,
		responsive: [
			{
				breakpoint: 767,
				settings:{
					adaptiveHeight: true
				}
			}
		]
	}); // end slider
	// import font
	window.WebFontConfig = {
		google: { families: ['Roboto Slab','Quicksand', 'Pattaya', 'Lato:400,900'] },
		active: function() {
		sessionStorage.fonts = true;
		}
	};
	(function() {
		var wf = document.createElement('script');
		wf.src = 'https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js';
		wf.type = 'text/javascript';
		wf.async = 'true';
		var s = document.getElementsByTagName('script')[0];
		s.parentNode.insertBefore(wf, s);
	})();
	
	// end import webfont

	// tabs function
	const checkTabs = $('.subwrap').hasClass('horizon-tabs');
	if (checkTabs){
		$('.horizon-tabs .subitems a').on('click', function(evt){
			// alert('ahihi');
			// evt.preventDefault();
			$('.subitems').removeClass('is-actived');
			$(this).closest('.subitems').addClass('is-actived');
			const id = $(this).attr('href').replace('#','');
			$('.horizon-content-tabs > div').removeClass('is-actived');
			$('.horizon-content-tabs > div#' + id +'').addClass('is-actived');
		});
	}
	// end tabs
	const checkArTabs = $('div').hasClass('article-tabs');
	if (checkArTabs){
		$('.tabs').tabs();
	}
	$('.sidenav').sidenav();
	$('window').resize(function(){
		$('.sidenav').sidenav();
	});
});

$("#searchbtn").on("click", function() {
	var value = $('#inputsearch').val().toLowerCase();
	value = value.replace(/(à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ)/g, "a");
	value = value.replace(/(è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ)/g, "e");
	value = value.replace(/(ì|í|ị|ỉ|ĩ)/g, "i");
	value = value.replace(/(ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ)/g, "o");
	value = value.replace(/(ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ)/g, "u");
	value = value.replace(/(ỳ|ý|ỵ|ỷ|ỹ)/g, "y");
	value = value.replace(/(đ)/g, "d");
	$("#doc-01 tbody tr").filter(function() {
		var temp = $(this).children('.column-2').text().toLowerCase();
		temp = temp.replace(/(à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ)/g, "a");
		temp = temp.replace(/(è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ)/g, "e");
		temp = temp.replace(/(ì|í|ị|ỉ|ĩ)/g, "i");
		temp = temp.replace(/(ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ)/g, "o");
		temp = temp.replace(/(ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ)/g, "u");
		temp = temp.replace(/(ỳ|ý|ỵ|ỷ|ỹ)/g, "y");
		temp = temp.replace(/(đ)/g, "d");
		$(this).toggle(temp.indexOf(value) > -1)
		console.log('temp '+temp)
	});
	console.log('value '+value)
});