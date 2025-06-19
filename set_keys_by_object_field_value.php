<?php
// https://stackoverflow.com/questions/70626615/array-of-objects-set-keys-by-object-field-value
$demo = [
    (object) ['key' => 'a', 'xxx' => 'xxx'],
    (object) ['key' => 'b', 'xxx' => 'xxx'],
    (object) ['key' => 'c', 'xxx' => 'xxx']
];

print_r(array_combine(array_column($demo, 'key'), $demo));
