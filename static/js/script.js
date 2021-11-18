jQuery(document).ready(function($) {

     // Vérification 
     $('#link').on('change keyup paste', () => {

        $('#extract').prop('disabled', () => {
            if ($('#link').val() == "") {
                return true;
            } else {
                return false;
            }
        });
    });
    $('#extract').click(function(){
	        $('#extract').html("Traitement en cours ...");
			var link = $('#link').val(),
			site_url = $(' #site_url').val();
			$.ajax({
				method: "POST",
				url:"/scrapp_web",
				dataType:'text',
				contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
				data:{ link : link}
			}).done(function( msg ) {
				
				$("#extractForm").get(0).reset();
				var parsedJson = $.parseJSON(msg);
				var data_name = "<tr><th>Nom de l'application</th><td>"+parsedJson.app_name+"</td></tr>";
				var data_version = "<tr><th>Version de l'application</th><td>"+parsedJson.app_version+"</td></tr>"
				var data_date = "<tr><th>Date de sortie de l'application</th><td>"+parsedJson.date_sortie+"</td></tr>"
				var data_desc = "<tr><th>Description de l'application</th><td>"+parsedJson.app_description+"</td></tr>"
				var data_nbre_download = "<tr><th>Nombre de téléchargement de l'application</th><td>"+parsedJson.app_nbre_downloads+"</td></tr>"

				var resultat = "<table>"+data_name+data_version+data_nbre_download+data_date+data_desc+"</table>";

				$('#block_resultat').show();
				$('#resultat').html(resultat);
				$('#extract').html("Extraire les contenus");
		})
			.fail(function( msg ) {
				alert('Opération non-réussie');
			});

		});
});


