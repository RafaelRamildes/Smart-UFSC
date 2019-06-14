
function changeLogin() {
	var loginInput = $('#username');
	var senhaInput = $('#password');
	var selectedUserType = $('#tipoDeAcesso option:selected').val();
	var admin = $('#admin').val();
	
	if (selectedUserType == 'alunoGraduacao' || selectedUserType == 'alunoPosGraduacao') {
		loginInput.attr('placeholder', 'Matrícula');
	} else if (selectedUserType == 'funcionario') {
		loginInput.attr('placeholder', 'SIAPE');
	} else if (selectedUserType == 'cadastroEspecial') {
		loginInput.attr('placeholder', 'Matrícula, CPF ou E-Mail');
	} else if (selectedUserType == 'pessoa') {
		loginInput.attr('placeholder', 'Login');
	} else if (selectedUserType == 'padrao') {
		loginInput.attr('placeholder', 'Matrícula, CPF, Passaporte, idUFSC ou E-mail');
	}
	
	loginInput.val('');
	if (admin == null || admin.value != '1') {
		senhaInput.val('');
	}

	loginInput.focus();		
}

if (!jqueryReady) {
	function jqueryReady() {
		if ($('#username').val()) {
			$('#password').focus();
		} else {
			$('#username').focus();
		}
		
		$('#tipoDeAcesso').change(changeLogin);
	}
}