function fib($n) {
    $a = 1;
    $b = 1;

    for ($i = 0; $i < $n; $i++) {
        echo "$a ";
        $c = $a;
        $a = $b;
        $b += $c;
    }
}

fib(1000);
