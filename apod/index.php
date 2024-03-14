
<?php
//SECTION: OBTENER RESULTADOS DE LA API
if (isset($_POST['picturedate']) && $_POST['picturedate']!="") {
	$picturedate = $_POST['picturedate'];
} else {
      $picturedate = date("Y-m-d");
}
$url = "https://api.nasa.gov/planetary/apod?date=$picturedate&concept_tags=True&api_key=";
$curlconn = curl_init($url);
curl_setopt($curlconn, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curlconn, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curlconn, CURLOPT_SSL_VERIFYPEER, false);
$response = curl_exec($curlconn);
$code = curl_getinfo($curlconn, CURLINFO_HTTP_CODE);
echo '<h1>NASA APOD API CALL</h1>
     <p>The NASA API requests must be made over HTTPS.</p>
     <p>Returned http code: '.$code.'
      </p><br><hr>';
      curl_close($curlconn);
//var_dump($response);
//SECTION: IMPRIMIR RESULTADOS
$result = json_decode($response);
echo "$picturedate";
echo "<center><img id='fetched-img' style='width:1080px;height:auto;' src='$result->url'></img></center>";
echo "<center><table>";
if (!empty($result->copyright)) {
      echo "<tr><td>Copyright:</td><td>$result->copyright</td></tr>";
}
echo "</table></center>";
?>


<script>
async function downloadImage() {
  const image = document.querySelector('#fetched-img')

  if (!image) {
      alert(' Algo paso')
      return
  }
  //esto es raro
  const imageBlog = await image.blob()
  const imageURL = URL.createObjectURL(imageBlog)

  const link = document.createElement('a')
  link.href = imageURL
  link.download = 'image file name here'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)

  // esto es raro
}
</script>
<center>
<form action="" method="POST">
<label class="mb">Enter Order ID:</label>
<section class="mb">
      <label for="date">Seleccionar Fecha:</label>
      <input type="date" id="picturedate" name="picturedate" value="<?php date("Y/m/d"); ?>" min="2018-01-01" max="2024-03-31" />
</section>
<button type="submit" name="submit">Submit</button>
</form>
<button name="download-image" onclick="downloadImage()">Descargar imagen</button>
</center>
<style>
.mb {
margin-bottom: 1rem;
}
</style>