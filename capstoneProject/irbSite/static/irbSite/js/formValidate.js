	
	
	/**************Password VALIDATE************/
	function passwordCheck() {
		if (document.getElementById('password').value ==
		document.getElementById('confirm_password').value) {
		document.getElementById('match_Message').style.color = 'green';
		document.getElementById('match_Message').innerHTML = 'matching';
	  } else {
		document.getElementById('match_Message').style.color = 'red';
		document.getElementById('match_Message').innerHTML = 'not matching';
	  }
	}
	
	
	
	/**************NUMBER VALIDATE************/
	
	function nextPrev(1) {
		var x, text;

		// Get the value of the input field with id="phone_num1"
		x = document.getElementById("phone_num1").value;

		// If x is Not a Number or less than one or greater than 10
		if (isNaN(x) || x < 1 || x > 10) {
			text = "Input not valid";
		} else {
			text = "Input OK";
		}
		document.getElementById("demo").innerHTML = text;
	}
	
