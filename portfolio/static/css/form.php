<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    Check the details given:<br>
    Name:
    <?php
    echo $_POST["fname"];
    echo $_POST["lname"];
    ?><br>
    Selected Subject:
    <?php
    echo $_POST["sub"];
    ?><br>
    Email:
    <?php
    echo $_POST["email"];
    ?><br>
    Age Group:
    <?php
    echo $_POST["age"];
    ?><br>
    Image:
    <?php
    echo $_POST["img"];
    ?><br>
</body>

</html>