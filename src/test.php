	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>SPAM DETECTOR</title>
<link rel="stylesheet" type="text/css" href="view.css" media="all">
<script type="text/javascript" src="view.js"></script>

</head>
<body id="main_body" >
	
	<img id="top" src="top.png" alt="">
	<div id="form_container">
	
		<h1><a>SPAM DETECTOR</a></h1>
		<form id="form_6911" name="detector" class="appnitro"  method="POST">
					<div class="form_description">
			<h2>SPAM DETECTOR</h2>
			<p>Web-Based App, integrated with Twitter API for Detecting Spam Tweets</p>
		</div>						
			<ul >
			
					<li id="li_3" >
		<label class="description" for="element_3">Choose Algorithm</label>
		<div>
		<select class="element select medium" id="element_3" name="element_3"> 
			<option value="" selected="selected"></option>
<option value="KMP" >KMP</option>
<option value="BM" >Boyer-Moore</option>
<option value="Regex" >Regex</option>


		</select>
		</div> 
		</li>		<li id="li_4" >
		<label class="description" for="element_4">Choose Tweet Type</label>
		<div>
		<select class="element select medium" id="element_4" name="element_4"> 
			<option value="" selected="selected"></option>
<option value="1" >User-Based</option>
<option value="2" >Region-Based</option>

		</select>
		</div> 
		</li>		<li id="li_1" >
		<label class="description" for="element_1">Enter Tweets Type </label>
		<div>
			<input id="element_1" name="element_1" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_2" >
		<label class="description" for="element_2">Enter Spam Query </label>
		<div>
			<input id="element_2" name="element_2" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>
			
					<li class="buttons">
			    <input type="hidden" name="form_id" value="6911" />
			    
				<input id="saveForm" class="button_text" type="button" name="submit" value="Submit" />
				</li>	
			</ul>
		</form>
		<div id = 'hasil'>

		</div>

				
		<div id="footer">
		</div>
	</div>
	<img id="bottom" src="bottom.png" alt="">
	<script>
		$("#saveForm").click(function() {
			var algo = document.detector.element_3.value;
			var search_type = document.detector.element_4.value;
			var text = document.detector.element_1.value;
			var spam_indicator = document.detector.element_2.value;

			var data_in = {};
			data_in.spam_indicator = spam_indicator;
			data_in.search_type = search_type;
			data_in.count = 20;
			if (search_type == "1") {
				data_in.username = text;
			}	
			else {
				data_in.region = text;
			}
			data_in = JSON.stringify(data_in);
			console.log(data_in);
			$.ajax({
				method : 'POST',
				headers: 'Access-Control-Allow-Origin : *',
				url : "http://127.0.0.1:5000/" + algo,
				data : {hasil : data_in}

			}).done(function(result){
				keluar = JSON.parse(result);
				var i;
				if (search_type == "1") {
					$("#hasil").append("<br>" + "SPAM INDIKATOR : " + spam_indicator + "<br>" + "USERNAME : " + text + "<br><br> BERIKUT HASIL SEARCHING SPAM");
				} else {
					$("#hasil").append("<br>" + "SPAM INDIKATOR : " + spam_indicator + "<br>" + "REGION : " + text + "<br><br> BERIKUT HASIL SEARCHING SPAM");
				}
				for (i = 0; i<(keluar['full_text']).length; i++) {
					if (keluar['is_spam'][i]) {
						$("#hasil").append("<br><br>" + "INI SPAM!!");
						keluar['full_text'][i];
						$("#hasil").append("<br>" + keluar['full_text'][i]);


					} else {
						$("#hasil").append("<br><br>" + "INI BUKAN SPAM!!");
						keluar['full_text'][i];
						$("#hasil").append("<br>" + keluar['full_text'][i]);
					}

				}
				
			});
		});
		
	</script>
	</body>
</html>
