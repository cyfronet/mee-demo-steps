#!/usr/bin/ruby

size = 5
array = (1..size).map { rand(size) }

File.open("numbers.txt", "w") do |f|
  array.each { |n| f.puts(n) }
end
