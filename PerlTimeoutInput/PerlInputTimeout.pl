#!/usr/bin/perl

# Disclaimer: This script is only for educational purposes.
# Please use this at your own risk.
# Author: jsinix(jsinix.1337@gmail.com) 

# This is a script that demonstrates how to get input from keyboard 
# with a timeout. This can be useful at many places.

use strict;
use warnings;

sub ask_data {
    my ($tout) = @_;	
    my $answer;
    print "Enter the data before $tout seconds: ";
    eval {
        local $SIG{ALRM} = sub { die "timeout reading from keyboard" };
        alarm $tout;
        $answer = <STDIN>;
        alarm 0;
        chomp $answer;
    };
    if ($@) {
        die $@ if $@ ne "timeout reading from keyboard";
        $answer = 'No answer given';
    }
    return $answer;
}

my $data = ask_data('10');
print "nThe answer is: " . $data . "n";
