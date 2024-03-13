<?php
$curlconn = curl_init('https://api.nasa.gov/planetary/apod?concept_tags=True&api_key=l2yDLDY1vcLGO2aCYrBuSHOwIaQ6BkvMq9BxKx8l');
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

$result = json_decode($response);
echo "<center><img style='width:1080px;height:auto;' src='$result->url'></img></center>";
echo "<center><table>";
echo "<tr><td>Copyright:</td><td>$result->copyright</td></tr>";
echo "</table></center>";
?>