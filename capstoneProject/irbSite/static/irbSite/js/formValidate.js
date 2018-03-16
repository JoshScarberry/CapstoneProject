	
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
		
		
		// the baic regx for phone numbers and emails
		// var phones = document.getElementById("phone").value;
		// var email = document.getElementById("emails").value;
		// var valid = true;
		//if (phones == "" || /\d{3}[ \-\.]?\d{3}[ \-\.]?\d{4}/.test(phones)) 
		//{
		//document.getElementById("err6").innerHTML = "Not a valid phone number";
			//valid = false;
		//}
		//if (email == "" || /^[\w.-]+@[\w.-]+\.[A-Za-z]{2,6}$/.test(email)) 
		//{
		//document.getElementById("err8").innerHTML = "Not a valid email";
			//valid = false;
		//}
	}