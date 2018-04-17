	
	//Validate Password
	function myFunction() {	
		var myInput = document.getElementById("confirm_password");
		var myInput2 = document.getElementById("password");
		var letter = document.getElementById("letter");
		var capital = document.getElementById("capital");
		var number = document.getElementById("number");
		var length = document.getElementById("length");
		var match = document.getElementById("match");
		
		// When the user clicks on the password field, show the message box
		myInput.onfocus = function() {
			document.getElementById("message").style.display = "block";
		}

		// When the user starts to type something inside the password field
		myInput.onkeyup = function() {
		  // Validate lowercase letters
		  var lowerCaseLetters = /[a-z]/g;
		  if(myInput.value.match(lowerCaseLetters)) {  
			letter.classList.remove("invalid");
			letter.classList.add("valid");
		  } else {
			letter.classList.remove("valid");
			letter.classList.add("invalid");
		  }
		  
		  // Validate capital letters
		  var upperCaseLetters = /[A-Z]/g;
		  if(myInput.value.match(upperCaseLetters)) {  
			capital.classList.remove("invalid");
			capital.classList.add("valid");
		  } else {
			capital.classList.remove("valid");
			capital.classList.add("invalid");
		  }

		  // Validate numbers
		  var numbers = /[0-9]/g;
		  if(myInput.value.match(numbers)) {  
			number.classList.remove("invalid");
			number.classList.add("valid");
		  } else {
			number.classList.remove("valid");
			number.classList.add("invalid");
		  }
		  
		  // Validate length
		  if(myInput.value.length >= 8) {
			length.classList.remove("invalid");
			length.classList.add("valid");
		  } else {
			length.classList.remove("valid");
			length.classList.add("invalid");
		  }
		  
		  // Validate Matching
			if (document.getElementById('password').value ==
			  document.getElementById('confirm_password').value) {
			  match.classList.remove("invalid");
			  match.classList.add("valid");
			  $('#confirm_password').css('border-color', 'lime');
		    } else {
			  match.classList.remove("valid");
			  match.classList.add("invalid");
			  $('#confirm_password').css('border-color', 'red');
		    }
		  
		}
	}
	
		
	//Show your Password
	function showFunction() {
		var x = document.getElementById("password");
		if (x.type === "password") {
			x.type = "text";
		} else {
			x.type = "password";
		}
		var x = document.getElementById("confirm_password");
		if (x.type === "password") {
			x.type = "text";
		} else {
			x.type = "password";
		}
	}
	
	
	
	/**************PHONE AND EMAIL VALIDATION************/
		function phoneemailFunction() {
			var phones = document.getElementById("tel").value;
			var email = document.getElementById("email").value;
			var valid = true;
			if (phones == "" || /\d{3}[ \-\.]?\d{3}[ \-\.]?\d{4}/.test(phones)) 
			{
			document.getElementById("err6").innerHTML = "Not a valid phone number";
				valid = false;
			}
			if (email == "" || /^[\w.-]+@[\w.-]+\.[A-Za-z]{2,6}$/.test(email)) 
			{
			document.getElementById("err8").innerHTML = "Not a valid email";
				valid = false;
			}
		}
	
	/**************Password VALIDATE************/
	/**function passwordCheck() {
		if (document.getElementById('confirm_password').value ==
		document.getElementById('password').value) {
		document.getElementById('match_Message').style.color = 'green';
		document.getElementById('match_Message').innerHTML = 'matching';
	  } else {
		document.getElementById('match_Message').style.color = 'red';
		document.getElementById('match_Message').innerHTML = 'not matching';
	  }
	}**/
	