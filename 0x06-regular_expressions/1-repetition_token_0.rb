#!/usr/bin/env ruby
# Ruby script to match a test_string with a regex

puts ARGV[0].scan(/hbt{2,5}n/).join
