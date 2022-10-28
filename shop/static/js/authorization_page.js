$('authorization_page').ready(function(){

    const RequestURL = 'http://127.0.0.1:8000/courcework/'

    function sendRequest(url) {
        return fetch(url).then(response => {
            return response.json()
        })
    }
    
    const wrongMessage = function(error){
        $('#wrongMessage').html() = error;

    }



    $('#register').click(function(){
        let login = $('#login').val();
        let password = $('#password').val();
        let registrationRequest = RequestURL + 'registration' + '?login=' + login + '&password=' + password;
        sendRequest(registrationRequest)
            .then(response => {
                response['status'] === 0 ? wrongMessage(response['error']) : 
                $(location).attr('href',"http://127.0.0.1:8000/courcework");
            })
            .catch(error => alert(error))

    })

    $('#sign-in').click(function(){
        let login = $('#login').val();
        let password = $('#password').val();
        let authorizationRequest = RequestURL + 'log_in' + '?login=' + login + '&password=' + password;
        
        sendRequest(authorizationRequest)
            .then(response => {
                response['status'] === 0 ? wrongMessage(response['error']) : 
                $(location).attr('href',"http://127.0.0.1:8000/courcework");
            })
            .catch(error => alert(error))

    })

})