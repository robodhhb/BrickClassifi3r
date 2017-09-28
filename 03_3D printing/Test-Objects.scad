module big_round() {
    cube([4*7.8, 4*7.8, 9.6/3]);
    translate([2*7.8, 2*7.8, 9.6/3]) cylinder(d=4*7.8, h=9.6*2, $fn=128);
}

module big_square() {
    cube([4*7.8, 4*7.8, 9.6/3]);
    translate([0, 0, 9.6/3]) cube([4*7.8, 4*7.8, 2*9.6]);
}

module small_square() {
    cube([4*7.8, 4*7.8, 9.6/3]);
    translate([7.8, 7.8, 9.6/3]) cube([2*7.8, 2*7.8, 2*9.6]);
}

big_round();
translate([4*7.8+1, 0, 0]) big_square();
translate([0, 4*7.8+1, 0]) small_square();
