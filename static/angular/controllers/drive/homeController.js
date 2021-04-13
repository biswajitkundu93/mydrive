mainApp.controller("homeController",function($scope, $http){
	$scope.data={}
    $scope.init = function(){
        console.log("I am home")
    }

    $scope.data.form={
        name:"",
        email:"",
        password:"",
        password2:""
    }

    $scope.data.formStyle={
        name:"",
        email:"",
        password:"",
        password2:""
    }
	$scope.data.loggin={}
	$scope.data.loggin.form={
        username:"",
        password:"",
    }

    $scope.data.loggin.formStyle={
        username:"",
        password:"",
    }

    $scope.submitForm = function() {
		console.log($scope.data.form)
		var error = 0;
		if(!$scope.data.form.name) {
			$scope.data.formStyle.name = "is_invalid";
			error++;
		} else {
			$scope.data.formStyle.name = "";
		}
        if(!$scope.data.form.email) {
			$scope.data.formStyle.email = "is_invalid";
			error++;
		} else {
			$scope.data.formStyle.email = "";
		}
		if(!$scope.data.form.password) {
			$scope.data.formStyle.password = "is_invalid";
			error++;
		} else {
			$scope.data.formStyle.password = "";
		}
        if(!$scope.data.form.password2) {
			$scope.data.formStyle.password2 = "is_invalid";
			error++;
		} else {
			$scope.data.formStyle.password2 = "";
		}
        if($scope.data.form.password2!=$scope.data.form.password) {
			$scope.data.formStyle.password = "is_invalid";
			$scope.data.formStyle.password2 = "is_invalid";
			$.growl.error({ message: "Password not match!"});
			error++;
		} else {
			$scope.data.formStyle.password = "";
			$scope.data.formStyle.password2 = "";
		}
		if(error==0) {
			$http({
				method: 'POST',
				url:'/user/signup',
				data: $scope.data.form,
				headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			}).then(function(success){
				alert("Register success")
				window.location.replace("/")
				console.log(success)
			},function(error){
				alert("erroe")
				console.log(error)
			}
			);
		} else {
			console.log('error')
			// $.growl.error({ message: "Please fill the form correctly!"});
		}
	}



	$scope.logginsubmitForm = function() {
		console.log($scope.data.loggin.form)
		var error = 0;
		if(!$scope.data.loggin.form.username) {
			$scope.data.loggin.formStyle.username = "is_invalid";
			error++;
		} else {
			$scope.data.loggin.formStyle.name = "";
		}
		if(!$scope.data.loggin.form.password) {
			$scope.data.loggin.formStyle.password = "is_invalid";
			error++;
		} else {
			$scope.data.loggin.formStyle.password = "";
		}
		if(error==0) {
			$http({
				method: 'POST',
				url:'/user/login',
				data: $scope.data.loggin.form,
				headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			}).then(function(success){
				alert("success")
				console.log(success)
				window.location.replace("/")
			},function(error){
				alert("erroe")
				console.log(error)
			}
			);
		} else {
			console.log('error')
			// $.growl.error({ message: "Please fill the form correctly!"});
		}
	}
})