var w,h,ch,c_h;
var cor_h = 0;
var debug = false;
var scroll_top = 0;
var helper_timer;	var helper_delay = 5000;
var scroll_timer;	var scroll_delay = 500;
var bubble_timer;	var bubble_delay = 2500; var bubble_move_t = 3000; var bubble_dis_t = 500; bubble_on=false;
var resize_timer;	var resize_delay = 250;
var hash_timer;		var hash_delay 	 = 2000;
var paralax_timer;	var paralax_delay = 10;
var fps_timer; var fps_counter; var fps_false_counter;

var scroll_run = false;

var swing_timer;
var page = $("html,body");
var body_height = 0;
var body_scroll = 0;
//================================================================================================================================================

function rand(min,max){	return Math.floor(Math.random() * (max - min + 1)) + min; }

//================================================================================================================================================

function new_bubble(){
	var eases = ['easeInQuad','easeInOutQuad','easeInCubic','easeInOutCubic','easeInOutExpo','easeInSine','easeInOutSine','easeInCirc','easeInOutCirc','easeInBack','easeInOutBack'];//easeInElastic
	var size = rand(10,25)/100;
	var l_e = eases[rand(0,eases.length-1)]; var b_e = eases[rand(0,eases.length-1)];
	$('<div class="bubble corner color_'+rand(1,4)+'"><span><span></span></span></div>').appendTo('#zed').animate({'width':(h*size),'height':(h*size)},rand(1500,2500),'easeOutQuad',function(){ 
		$(this).css({'right':'auto','left':(w*0.89-h*size)});
		$(this).removeClass('corner').addClass('bubble_anim').animate({'left':[rand(w/10,w/10*6),l_e],'bottom':[h*(1+2*size),b_e],'opacity':[0,'easeInExpo']},rand(4000,8000),function(){
			$(this).remove();
		});
	});
}


var anchors = {
	'jsem-dite':0,  //set scroll values here in the decreasing sequence
	'jsem-rodic':2.9,
	'jsem-nasilny':4.6,
	'vim-o-nasili':6.3
}

var images = {
	'zed_grafiti'	:{'url':'zed2.gif','size':195.6},
	'bytustka'		:{'url':'bytustka_balonky_3.png','size':34.0,'selector':'#bytustka > div'},
	'bytustka_telo'	:{'url':'bytustka_zavesena.png','size':8.2},
//	'pradlo' 		:{'url':'pradlo.png','size':19.2},
//	'pradlo_s' 		:{'url':'pradlo_s2.png','size':5.9},
	'zed_bytustka'	:{'url':'bytustka_zed2.png','size':13.7},
//	'zed_schranka'	:{'url':'zed_schranka-hover.png','size':18},
//	'zed_kocka'		:{'url':'kocka.png','size':1.7},
	'firefox'		:{'url':'b_firefox.png','size':17.2},
	'logo'			:{'url':'bytustka_logo.png','size':16.3},
	'socials1'		:{'url':'socials_zed.png','size':42.2,'selector':'#zed a.socials'},
	'bubble_1'		:{'url':'bublina_odraz.png','size':1.4,'selector':'#bubble_1 > span > span'},
	'zed_top'		:{'url':'zed2top.png','size':63.9},
//	'tuje' 			:{'url':'tuje.png','size':36},
	'dum1' 			:{'url':'dum1.png','size':665.7},
	'dum1_in' 		:{'url':'dum1-in-3.png','size':22.1},
//	'dum1_obrazek'	:{'url':'dum1-obrazek.png','size':10.2},
//	'dum1_stroj'	:{'url':'dum1-in-stroj.png','size':4.1},
	'dum1_tyran'	:{'url':'bytustka_anim_tyran-barva-pozadi.gif','size':78.7},
	'vetev' 		:{'url':'vetev.png','size':31.5},
	'hnizdo'		:{'url':'bytustka_anim_ptak-2.gif','size':153},//{'url':'hnizdo.png','size':5.1},
	'panel1' 		:{'url':'panel1_2.png','size':1126},
	'dum2' 			:{'url':'dum2.png','size':318.1},
//	'dum2_in' 		:{'url':'dum2-in.jpg','size':4.2},
	'panel2'		:{'url':'panel2_3.png','size':710.1},
	'komin'			:{'url':'komin2.png','size':94.7,'selector':'#komin_bg'},
//	'jerab'			:{'url':'jerab2.png','size':86.8},
//	'mrak1'			:{'url':'mrak1.png','size':27.2},
	'balon'			:{'url':'balon_3.png','size':174.3},
//	'balon_pilot'	:{'url':'bytustka_anim_balon-telo-2.gif','size':23.2},
//	'balon_praporek':{'url':'praporek.gif','size':21.1},
//	'mrak2'			:{'url':'mrak2.png','size':18.2},
//	'mrak3'			:{'url':'mrak3.png','size':13.8},
	'princ'			:{'url':'princ_3.png','size':54.8},
//	'princ_sala'	:{'url':'sala.gif','size':12.9},
	'claim'			:{'url':'claim2.png','size':45.5},
	'pozadi'		:{'url':'pozadi4a.jpg','size':330.9},
	'pozadi_b'		:{'url':'pozadi4b.jpg','size':469.7,'selector':'#pozadi > div'},
	'zalozka'		:{'url':'zalozky_42.png','size':40.8,'selector':'.zalozka'},
	'socials2'		:{'url':'socials_space.png','size':14.4,'selector':'#socials a.socials'},
	'bublina_L'		:{'url':'bublina_L.png','size': 6.5,'selector':'#bublina_L > div'},
	'bublina_R'		:{'url':'bublina_R.png','size': 8.6,'selector':'#bublina_R > div'},
	'bublina_T'		:{'url':'bublina_T.png','size':20.0,'selector':'#bublina_T > div'},
//	'bytustka_text1':{'url':'bytustka_balonky_text1_.png','size': 1.9,'selector':'#bytustka > div > .bublina > a,#bublina_T > div > div > a'},
//	'bytustka_text2':{'url':'bytustka_balonky_text2.png','size': 5.6,'selector':'#bytustka > div > #bytustka_link_muj_pribeh, #bytustka_link_muj_pribeh > span, #bytustka > div > #bytustka_link_zpet, #bytustka > div > #bytustka_link_zpet > span, #bytustka_link_muj_pribeh_2'},
//	'bytustka_text3':{'url':'bytustka_balonky_text3_.png','size': 0.7,'selector':'#bytustka_link_vim_o_nasili,#bytustka_link_vim_o_nasili_2'},
	'dum2_in_anim' 	:{'url':'bytustka_anim_kolibka2.gif','size':71.6},
//	'cap' 			:{'url':'bytustka_anim_cap-komplet-delsi-70-procent.gif','size':94.3},
	'scroll_helper'	:{'url':'b_sipka.png','size':6.8},
	'page_pribeh'	:{'url':'pribeh_pozadi.jpg',		'size':353.7},
//	'papir_top'		:{'url':'pribeh_papir_top.png',		'size': 32.8,	'selector':'#page_pribeh div.papir .papir_top'},
//	'papir_left'	:{'url':'pribeh_papir_left.png',	'size': 12.4,	'selector':'#page_pribeh div.papir .papir_1'},
//	'papir_right'	:{'url':'pribeh_papir_right.png',	'size': 14.5,	'selector':'#page_pribeh div.papir .papir_2'},
	'papir'			:{'url':'pribeh_papir.jpg',			'size': 72.4,	'selector':'#page_pribeh div.papir .papir_3'},
	'underline'		:{'url':'h1_underline.png',			'size':  0.4,	'selector':'#page_pribeh div.papir .text h1'},
	'stroj_back'	:{'url':'pribeh-stroj-back.png',	'size':  8.2,	'selector':'#page_pribeh div.stroj_back'},
//	'stroj'			:{'url':'pribeh_stroj.png',			'size':110.3,	'selector':'#page_pribeh div.stroj'},
	'page_info'		:{'url':'b_o-bytustce-podklad.png',	'size':236.6 },
}
var images_en = {
	'bytustka'		:{'url':'bytustka_balonky_3.en.png','size':30.4,'selector':'#bytustka > div'},
	'panel2'		:{'url':'panel2_3.en.png','size':653.4},
	'claim'			:{'url':'claim2.en.png','size':34.8},
	'bublina_L'		:{'url':'bublina_L.en.png','size': 4.2,'selector':'#bublina_L > div'},
	'bublina_R'		:{'url':'bublina_R.en.png','size': 7.5,'selector':'#bublina_R > div'},
	'bublina_T'		:{'url':'bublina_T.en.png','size':16.1,'selector':'#bublina_T > div'},
	'bytustka_text2':{'url':'bytustka_balonky_text2.en.png','size': 3.7,'selector':'#bytustka > div > #bytustka_link_muj_pribeh, #bytustka_link_muj_pribeh > span, #bytustka > div > #bytustka_link_zpet, #bytustka > div > #bytustka_link_zpet > span, #bytustka_link_muj_pribeh_2'},
	'logo'			:{'url':'bytustka_logo.en.png','size':11.5},
}



var images_param = '?x='+Math.random();
var images_loaded = 0;
var images_size = 0;
var images_size_loaded = 0;
var images_count = Object.keys(images).length;

var objects = {
	'pradlo':	{'w':1.00,	'cw':0						,'s0':{'s':0.0,	'b': 0.60,	'l': 0.0 },	's1':{'s':1.00,	'b': 0.4,	'l': 0.00 }},
	'pradlo_s':	{'w':1.00,	'cw':0						,'s0':{'s':0.0,	'b': 0.54,	'l': 0.0 },	's1':{'s':1.00,	'b': 0.62,	'l': 0.00 }},
	'tuje':		{'w':0.14,	'cw':430/976	,'h':0.32	,'s0':{'s':0.0,	'b':-0.10,	'r': 0.1 },	's1':{'s':0.32,	'b': 0.0,	'r':-0.05 }},
	'dum1':		{'w':0.42,	'cw':800/1949	,'h':1.02	,'s0':{'s':0.0,	'b':-0.30,	'l': 0.0 },	's1':{'s':1.02,	'b': 0.0,	'l':-0.20 }},
	'dum1_in':	{'w':0.13,	'cw':253/1293	,'h':0.66	,'s0':{'s':0.0,	'b':-0.20,	'l': 0.12},	's1':{'s':0.80,	'b': 0.3,	'l':-0.03 }},
	'dum1_over':{'w':0.13,	'cw':253/1293	,'h':0.66	,'s0':{'s':0.0,	'b':-0.20,	'l': 0.12},	's1':{'s':0.80,	'b': 0.3,	'l':-0.03 }},
	'panel1':	{'w':0.70,	'cw':1120/2191	,'h':1.37	,'s0':{'s':0.0,	'b':-0.20,	'r': 0.0 },	's1':{'s':1.77,	'b': 0.4,	'r':-0.30 }},
	'vetev':	{'w':0.50,	'cw':800/356	,'h':0.23	,'s0':{'s':1.7,	'b': 1.90,	'r': 0.0 },	's1':{'s':1.93,	'b': 1.7,	'r':-0.15 }},
	'dum2':		{'w':0.50,	'cw':640/1440	,'h':1.13	,'s0':{'s':1.1,	'b': 1.10,	'r': 0.0 },	's1':{'s':3.23,	'b': 2.1,	'r':-0.15 }},
	'dum2_in':	{'w':0.13,	'cw':200/400	,'h':0.26	,'s0':{'s':2.1,	'b': 2.10,	'r': 0.15},	's1':{'s':3.00,	'b': 2.75,	'r': 0.09 }},
	'panel2':	{'w':0.70,	'cw':800/1824	,'h':1.6	,'s0':{'s':0.0,	'b':-0.30,	'l': 0.0 },	's1':{'s':4.10,	'b': 2.5,	'l':-0.30 }},
	'komin':	{'w':0.20,	'cw':480/1144	,'h':0.48	,'s0':{'s':2.5,	'b':  2.3,	'l': 0.20},	's1':{'s':5.60,	'b': 4.92,	'l': 0.18 }},
//	'jerab':	{'w':0.75,	'cw':1200/1270	,'h':0.80	,'s0':{'s':1.7,	'b': 1.40,	'l': 0.30},	's1':{'s':4.30,	'b': 3.50,	'l': 0.36 }},
	'text3':	{'w':0.40,	'cw':3/5		,'h':0.66	,'s0':{'s':3.0,	'b':  3.0,	'r': 0.05},	's1':{'s':5.26,	'b': 4.6,	'r': 0.05 }},
	'mrak1':	{'w':1.20,	'cw':1360/415	,'h':0.37	,'s0':{'s':4.8,	'b':  4.8,	'l':-0.05},	's1':{'s':7.50,	'b': 7.1,	'l':-0.05 }},
	'balon':	{'w':0.40,	'cw':640/1098	,'h':0.69	,'s0':{'s':4.7,	'b':  4.7,	'r': 0.10},	's1':{'s':7.80,	'b': 7.0,	'r': 0.10 }},
	'text4':	{'w':0.40,	'cw':3/5		,'h':0.6	,'s0':{'s':4.3,	'b':  4.3,	'l': 0.05},	's1':{'s':7.30,	'b': 6.6,	'l': 0.05 }},
//	'mrak2':	{'w':0.80,	'cw':1360/243	,'h':0.15	,'s0':{'s':6.1,	'b':  6.1,	'r': 0.10},	's1':{'s':7.60,	'b': 7.45,	'r': 0.05 }},
//	'mrak3':	{'w':1.20,	'cw':1180/187	,'h':0.19	,'s0':{'s':6.1,	'b':  6.1,	'l':-0.10},	's1':{'s':6.90,	'b': 6.70,	'l':-0.10 }},
	'princ':	{'w':0.30,	'cw':423/663	,'h':0.47	,'s0':{'s':7.0,	'b':  7.0,	'l': 0.11},	's1':{'s':8.42,	'b': 8.1,	'l': 0.03 }},
	'claim':	{'w':0.50,	'cw':1200/680	,'h':0.29	,'s0':{'s':8.1,	'b':  8.1,	'l': 0.25},	's1':{'s':8.42,	'b': 8.53,	'l': 0.25 }},
	'socials':	{'w':0.21,	'cw':336/112	,'h':0.07	,'s0':{'s':8.8,	'b':  8.8,	'r': 0.00},	's1':{'s':8.87,	'b': 8.8,	'r': 0.00 }},
	'pozadi':	{'w':1.00,	'cw':1600/4821	,'h':3.01	,'s0':{'s':1.2,	'b':  0.8,	'r': 0.00},	's1':{'s':8.42, 'b': 6.1,	'r': 0.00 },'bg':true},
//	'bytustka':	{'w':0.30,	'cw':480/831	,'h':0.52	,'s0':{'s':1.0,	'b': -0.3,	'r': 0.05},	's1':{'s':8.00,	'b': 8.0,	'r': 0.35 }},
	'bublina_L':{'w':0.09,	'cw':175/175	,'h':0.09	,'s0':{'s':8.3,	'b':  8.3,	'l': 0.11},	's1':{'s':8.42, 'b': 8.75,	'l': 0.06 }},
	'bublina_R':{'w':0.11,	'cw':203/201	,'h':0.11	,'s0':{'s':7.8,	'b':  7.8,	'l':-0.05},	's1':{'s':8.42, 'b': 8.60,	'l': 0.02 }},
	'bublina_T':{'w':0.22,	'cw':353/334	,'h':0.2	,'s0':{'s':7.2,	'b':  7.2,	'l': 0.70},	's1':{'s':8.42, 'b': 8.45,	'l': 0.76 }},
};

var bytustka_x = {
	  0:	0.65,
	 30: 	0.25,
	 70:	0.40,
	160:	0.90,
	150:	0.75,
	200:	0.60,
	300:	0.75,
	370:	0.45,
	490:	0.60,
	491:	1.10,
	600:	0.75,
	700:	1.60,
	999:	1.60
}

function init_document(){
//	w = $(window).width(); 
//	h = $(window).height();
	//on_resize();
	get_dimensions();

	// vypocet potrebne vysky dokumentu
	c_h = 0; $.each(objects,function(id){
		$('#'+id).width(this.w * w);
		if(this.cw > 0){
			var oh = this.w / this.cw * w;
			$('#'+id).css('height',oh);
			if(this.bg!=true) c_h = Math.max(c_h,oh + this.s1.b*w + h);
		}
	});
	

	// zobrazeni intra (zed) a priprava body
	//stop(true).removeClass('hidden').css('opacity',1).delay(500)
	$('#landscape_white').delay(1000).animate({'opacity':0},2000,function(){ $(this).addClass('hidden');	});
	$('#pradlo,#pradlo_s').removeClass('hidden').css('opacity',0).delay(2500).animate({'opacity':1},1500);
	
	$('#zed').css({'width':w,'height':h});
	$('#zed_grafiti').css('opacity',1);
//	$('#zed_grafiti').animate({'opacity':1},2000,function(){
		$('#body_wrapper').height(c_h);
		$('#pradlo,#pradlo_s').height(h / 3.75);
		$('body').css({'width':w,'height':c_h+cor_h});
		$('body').removeClass('not_ready').addClass('ready');
		try{ clearInterval(bubble_timer); }catch(e){ }
		bubble_on=true; new_bubble(); bubble_timer = setInterval(new_bubble,bubble_delay);
		$(document).scrollTop(c_h-h);
		on_scroll();
		if(location.hash!='') scroll_to_hash();
		//$('#pradlo,#pradlo_s').removeClass('hidden').animate({'opacity':1},1000);

		$('a[data-anchor]').click(function(){	
			if($('#body_wrapper').hasClass('hidden')){
				hide_pribeh($(this).attr('data-anchor'));			
			}else{
				scroll_to(anchors[$(this).attr('data-anchor')]*1); 
			}
		});
//	});
	
	// pridani pravitek
	if(debug==true) for(var i=1;i<((c_h-h)/w)*10;i++) $('#tmp').after('<div class="ruler" style="bottom:'+(i*w/10+h)+'px"><span>'+(i/10)+'</span></div>');
	 $('#tmp').after('<div class="ruler" style="top:0px"><span>MAX</span></div>');
	
	// nacasovani napovedy
	helper_timer = setTimeout(function(){ 
		$('#scroll_helper').css('bottom',(h-0.12*w)/4).animate({'opacity':1},500);
//		helper_timer = setTimeout(function(){ 
//			$('#scroll_helper').animate({'opacity':0},500,function(){ $(this).remove(); });
//		}, helper_delay);
	}, helper_delay);
	
	fps_timer = setInterval(fps_scan,1000);
	$('#preloader').animate({'opacity':0},250,function(){ $(this).remove(); });
}


function fps_scan(){
	$('#fps').html(fps_counter+'fps (skiped '+fps_false_counter+')');
	fps_false_counter=0;
	fps_counter=0;
}



//================================================================================================================================================

function paralax_scroll(){
	paralax_timer = null;
	on_scroll();
}

function scroll_on(){
	scroll_run=false;
}

function on_scroll(){
	if(scroll_run==true){ fps_false_counter++; return; }

	scroll_run=true;
	// hlidani ukonceni scrollu
	clearTimeout(scroll_timer);	scroll_timer = setTimeout(scroll_stop,scroll_delay);


	// podstranky
	if($('#body_wrapper').hasClass('hidden')){ scroll_run=false; return; }

	// ochrana proti scrollu o zlomky pixelu
	
	if(Math.round(window.pageYOffset)==scroll_top || $('body').hasClass('not_ready')){ scroll_run=false; return; }
//	if(Math.round($(document).scrollTop())==scroll_top || $('body').hasClass('not_ready')){ scroll_run=false; return; }

	// ochrana proti prilis castemu volani
//	if(paralax_timer==null){
//		paralax_timer = setTimeout(paralax_scroll,paralax_delay);
		fps_counter++;
//	}else{
//		fps_false_counter++;
//		return;
//	}
	

	// vypocet pozice okna vuci obsahu (horni a dolni okraje okna)		
	scroll_top = Math.round(window.pageYOffset);
	//scroll_top = Math.round($(document).scrollTop());
	
	$('#landscape_cover').css({'top':scroll_top+h});
	var y = Math.floor(Math.max(0,(c_h - h - scroll_top)/w)* 1000)/1000; //- cor_h//cor_h - 
	var y2 = Math.floor((y - h / w )*1000)/1000;
	if(debug==true) $('#tmp').html('Y = <'+y+';'+y2+'><br />y = <'+scroll_top+';'+(scroll_top+h)+'><br />Ratio:'+(Math.round(w/h*1000)/1000)+'<hr />');	

	// kontrola a posun vsech objektu
	$.each(objects,function(id){
		if(y >= this.s0.s && y2 <= this.s1.s){
			var cy = (y - this.s0.s) / ((this.s1.s+h/w) - this.s0.s);
			if(debug==true) $('#tmp').append('OBJ['+id+']:show ('+Math.round(cy*1000)/1000+')<br />');	 //, H='+(this.w / this.cw)+'
			if($('#'+id).hasClass('hidden')) $('#'+id).removeClass('hidden');
			if(this.cw > 0){
				$('#'+id).css('bottom',((this.s1.b-this.s0.b)*cy+this.s0.b)*w + h);
			}else{
				$('#'+id).css('bottom',((this.s1.b-this.s0.b)*cy+this.s0.b)*h);
			}
			if(this.s0.l!='undefined') $('#'+id).css('left',(((this.s1.l-this.s0.l)*cy+this.s0.l)*w));
			if(this.s0.r!='undefined') $('#'+id).css('right',(((this.s1.r-this.s0.r)*cy+this.s0.r)*w));
		}else{
			if(!$('#'+id).hasClass('hidden')) $('#'+id).addClass('hidden');
			if(debug==true) $('#tmp').append('OBJ['+id+']:hidden<br />');	
		}
	});
	
	// kontrola letajici bytustky
	if(y2 < 0 && !$('#bytustka').hasClass('hidden') && !$('#bytustka').hasClass('leaving') && !$('#bytustka').hasClass('subpage')){
		if($('#bytustka').position().top + w*0.3/(480/831) < scroll_top){
			$('#bytustka').removeClass('anim').addClass('hidden');
		}else{
			$('#bytustka').removeClass('anim').addClass('leaving').addClass('za_zdi').stop(true).animate({'top':(c_h-h)},3000,function(){ $(this).addClass('hidden').removeClass('leaving').removeClass('za_zdi'); });	
			//,'left':w*1.1
		}
	}

	// kontrola animace bublin
	if(y2 < 0 && bubble_on==false){
		try{ clearInterval(bubble_timer); }catch(e){ }
		bubble_on=true; new_bubble(); bubble_timer = setInterval(new_bubble,bubble_delay);
	}else if(y2 > 0 && bubble_on==true){
		bubble_on=false; clearInterval(bubble_timer);
	}
	if(debug==true) $('#tmp').append('BUBBLES: '+((bubble_on)?'ON':'OFF')+'<br />');	
	
	// zruseni napovedy
	if($('#scroll_helper').length==1 && y > 0.1){
		clearTimeout(helper_timer);
		$('#scroll_helper').stop(true).animate({'opacity':0},500,function(){ $(this).remove(); });
	}
	
	//paralax_timer = 
	// setTimeout(scroll_on,100);
	scroll_run=false; 
}

function scroll_stop(){
	if(debug==true) $('#tmp').append('BYTUSTKA:check<br />');

	// postranka
	if($('#body_wrapper').hasClass('hidden')){
		scroll_top = Math.round($(document).scrollTop());
		$('#bytustka').removeClass('swing').removeClass('anim').animate({'top':scroll_top+h*0.05},2500,function(){  });	//.stop(true)
		swing_timer = setTimeout(function(){ $('#bytustka').addClass('swing'); }, 100);
		return;
	}

	// update letajici bytustky
	if(c_h - scroll_top - h > h){
//		$('#fps').html('UP');
		var y = Math.floor(Math.max(0,(c_h - h - $(document).scrollTop())/w)* 100)/1000;//change the balloon boy's trajectory here
		var y2 = Math.floor((y - h / w )*1000)/1000;
		var x0=bytustka_x[0]; var y0=0; var x1=-1; var y1=0; var x=0;
		$.each(bytustka_x,function(k){ if(y2 * 100 > k){ x0=this; y0=k/100; }else if(x1==-1){ x1=this; y1=k/100; if(debug==true) $('#tmp').append('['+x0+';'+y0+'] -> ['+x1+';'+y1+']<br />'); } });
		if(debug==true) $('#tmp').append('<0;1> = '+(y2-y0)/(y1-y0)+'<br />');
		var x = (y2-y0)/(y1-y0)*(x1-x0)+x0;
		//removed the appreance of the balloon kid here
		// if($('#bytustka').hasClass('hidden')) $('#bytustka').css({'top':(scroll_top + h),'opacity':1}).removeClass('hidden');
		$('#bytustka').removeClass('swing').removeClass('anim').stop(true).animate({'top':Math.max(h,scroll_top),'left':x*(w*0.7)},2500,function(){  });
		swing_timer = setTimeout(function(){ $('#bytustka').addClass('swing'); }, 100);
		if(debug==true) $('#tmp').append('->'+Math.max(h,scroll_top)+','+(x*100)+'%');
	}
}

function scroll_to(y,time){
//	$("html,body").animate({ scrollTop: 0 }, 2000);	
	t = c_h - h - (y * w);
//	alert('scroll_to:'+y+' ('+time+') => '+t);
	var dif = Math.abs(scroll_top - t);	if(time!=undefined) dif=time;
	if(dif>0){ $('html,body').stop(true).animate({ scrollTop: t },dif*0.75,'easeInOutSine'); }else{	$('html,body').stop(true).scrollTop(t); }
//,
}

function scroll_to_hash(){
	if(anchors[location.hash.replace('#','')]!=undefined) scroll_to(anchors[location.hash.replace('#','')]*1);
}

function preloaded(img){
	var id = $(img).attr('id').replace('preload_','');
	var selector = '#'+id; if(images[id].selector!=undefined) selector=images[id].selector;
	$(selector).css('background-image','url('+$(img).attr('src')+')');
	if(selector=='#zed_bytustka' || selector=='#logo') $(selector).css('opacity',0).animate({'opacity':1},1000);
	$(img).remove();
	images_loaded++; images_size_loaded+=images[id].size;
	$('#tmp').append('IMG['+id+'] loaded ('+images_loaded+'/'+images_count+') ('+Math.round(images_size_loaded)+'kB/'+Math.round(images_size)+'kB)<br />');
	$('#preloader .progress').css('width',Math.round(images_size_loaded/images_size*100)+'%');
	if(images_loaded == images_count){
		init_document();
		$(document).scroll(on_scroll);
		$('body').bind('touchmove', on_scroll);
		// document.addEventListener("touchmove", on_scroll, false);
		$(window).resize(on_resize);
	}
}

function show_pribeh(){
	body_height = $('body').height() * 1;
	body_scroll = $(document).scrollTop() * 1;
	bytustka_top = body_scroll - (w*0.39*0.64); //$('#bytustka > div').height()*0.64;
//	alert('BH:'+body_height+' BS:'+body_scroll+' BT'+bytustka_top+' BBH:'+$('#bytustka > div').height());
	clearTimeout(scroll_timer);
	$('#bytustka').removeClass('hidden').stop(true).animate({'top':bytustka_top},500,function(){
		$('#bytustka').addClass('bez_balonku').animate({'top':bytustka_top+h},2000);
		$('#page_pribeh').css({'height':0,'marginTop':0,'width':w}).addClass('fixed').removeClass('hidden').animate({'height':h},2000,function(){
			$('#body_wrapper').addClass('hidden');
			$(document).scrollTop(0);
			var ph = $('#page_pribeh > div').height();
			$('#page_pribeh').removeClass('fixed').css({'height':ph,'width':w});
			$('body').css('height',ph);
			$('#bytustka').removeClass('bez_balonku').addClass('subpage').stop(true).css({'top':h*0.05,'left':$('#bytustka').width()*-1 }).animate({'top':0,'left':40},1500);
		});
	});
}

function hide_pribeh(anchor){
	var ny = body_scroll;
	var sc_t = $(document).scrollTop();
	$('#page_pribeh').addClass('fixed').css({'height':sc_t+h,'marginTop':-sc_t});
	$('#body_wrapper').removeClass('hidden');
	$('body').height(body_height);
	if(anchor!=undefined){ scroll_to(anchors[anchor]*1,0); ny=c_h-h-(anchors[anchor]*w); }else $('html,body').scrollTop(ny);
	on_scroll();
	$('#page_pribeh').stop(true).animate({'height':sc_t},2000,function(){ $('#page_pribeh').removeClass('fixed').addClass('hidden'); });
	$('#bytustka').stop(true).removeClass('subpage').css({'top':ny+h*0.05});
}

function on_resize(){
//	alert('resize');
	var old_w=w; var old_h=h;
	get_dimensions();
	if(old_w==w && old_h==h) return;

	$('body').removeClass('ready').addClass('not_ready');
	$('#zed_grafiti').css('opacity',0);
	$('.ruler,#tmp').remove(); 
	$('body').css({'width':w,'height':c_h+cor_h});

	// hlidani ukonceni resize
	clearTimeout(resize_timer);	resize_timer = setTimeout(init_document,resize_delay);
	try{ clearInterval(bubble_timer); }catch(e){ }
}

function get_dimensions(){
	w=$(window).width(); h=$(window).height();
	if(h > w){
		h = w*2/3; cor_h = $(window).height()-h;
		$('#landscape_cover').removeClass('hidden').css({'height':cor_h});
		// $('#body_wrapper').css({'bottom':cor_h});
	}else{
		cor_h=0;
		$('#landscape_cover').addClass('hidden');
	}
	$('#zed').css({'height':h});
}

function show_info(){
	$('#page_info').css('opacity',0).removeClass('hidden').stop(true).animate({'opacity':1},500);
}

function hide_info(){
	$('#page_info').stop(true).animate({'opacity':0},500,function(){ 
		$(this).addClass('hidden'); 
	});
}

$(document).ready(function(){
	// debugovaci konzole
	if(debug==true) $('#zed').before('<div id="tmp"></div>');

	// nahrazeni EN obrazku
	if($('body').hasClass('en')){ 
//		alert('EN!');
		$.each(images_en,function(id){ 
//			alert(id+':'+this);
			images[id]=this; 
		}); 
	}

	get_dimensions();

	// preload obrazku
	var pre_html = '';
	$.each(images,function(id){ pre_html += '<img id="preload_'+id+'" src="./img/'+this.url+images_param+'" alt="" />'; images_size+=this.size; });
	$('#null').append(pre_html);
	$("#null > img").one("load", function() {
		preloaded(this);
	}).each(function() {
		if(this.complete) $(this).load();
	});
	
	$('#dum1_obrazek_link'	).mouseover(function(){ $('#dum1_obrazek').addClass('hover'); 	 });
	$('#dum1_obrazek_link'	).mouseout( function(){ $('#dum1_obrazek').removeClass('hover'); });
	$('#dum1_stroj_link'	).mouseover(function(){ $('#dum1_stroj'  ).addClass('hover'); 	 });
	$('#dum1_stroj_link'	).mouseout( function(){ $('#dum1_stroj'  ).removeClass('hover'); });

	$('a[data-href="pribeh"]').click(function(evt){
		show_pribeh();
		evt.stopPropagation();
		evt.preventDefault();
		return;
	});
	$('#bytustka_link_zpet').click(function(evt){
		hide_pribeh();
		evt.stopPropagation();
		evt.preventDefault();
		return;
	});
	
	
	// test na mobilu
	// setInterval(on_scroll,40);
	
});

