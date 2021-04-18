mainApp.controller("homeController",function($scope, $http){
	$scope.data={
		listData:[],
		listFileData:[],
		backList:[],
		parent:{},
		file:""
	}
    $scope.init = function(){
        console.log("I am home")
		$scope.openFolder(0)
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
				alert("Login")
				console.log(success)
				window.location.replace("/")
			},function(error){
				alert("error")
				console.log(error)
			}
			);
		} else {
			console.log('error')
			// $.growl.error({ message: "Please fill the form correctly!"});
		}
	}



	$scope.logout = function() {
			$http({
				method: 'POST',
				url:'/user/logout',
				headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			}).then(function(success){
				alert("Logout")
				console.log(success)
				window.location.replace("/")
			},function(error){
				alert("error")
				console.log(error)
			}
			);
	}

	$scope.data.foldername="";
	$scope.createFolder=()=>{
		var error = 0;
		if(!$scope.data.foldername) {
			$scope.data.foldername = "is_invalid";
			error++;
		} 
		if(error==0) {
			$http({
				method: 'POST',
				url:'/create-folder',
				data: {
					name:$scope.data.foldername,
					parent_id:$scope.data.parent.id
				},
				headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			}).then(function(success){
				alert("Folder create successfully")
				// window.location.replace("/");
				$scope.openFolder($scope.data.parent.id)
			},function(error){
				alert("error")
			}
			);
		} else {
			console.log('error')
			// $.growl.error({ message: "Please fill the form correctly!"});
		}
	}

	$scope.openFolder=(id)=>{
		console.log("=====================update=======================")
		console.log(id)
		$http({
			method: 'POST',
			url:'/open-folder',
			data: {
				id:id
			},
			headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
		}).then(function(success){
			$scope.data.listData = success.data.data.folderList
			$scope.data.listFileData = success.data.data.fileList
			$scope.data.parent = success.data.data.parent
			if (id!=0){
				$scope.data.backList.push(id)
				console.log($scope.data.backList)
			}
			console.log($scope.data)
		},function(error){
			alert("error")
		}
		);
		console.log("============================================")
		 
	}
	$scope.backFolder=()=>{
		console.log("call back")
		$scope.data.backList.pop();
		if ($scope.data.backList.length==0){
			$scope.openFolder(0)
		}
		else{
			$scope.openFolder($scope.data.backList.pop())
		}
	}


	$scope.uploadFile=()=>{
		var error = 0;
		if(!$scope.data.file) {
			$scope.data.file = "is_invalid";
			error++;
		} 
		if(error==0) {
			$http({
				method: 'POST',
				url:'/upload-file',
				data: {
					file:$scope.data.file,
					parent_id:$scope.data.parent.id
				},
				headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
			}).then(function(success){
				alert("File upload Successfully")
				console.log(success.data)
				$scope.data.file=""
				// window.location.replace("/");
				$scope.openFolder($scope.data.parent.id)
			},function(error){
				alert("error")
			}
			);
		} else {
			console.log('error')
			// $.growl.error({ message: "Please fill the form correctly!"});
		}
	}
})