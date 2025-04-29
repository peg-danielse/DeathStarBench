# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

# If CMAKE_DISABLE_SOURCE_CHANGES is set to true and the source directory is an
# existing directory in our source tree, calling file(MAKE_DIRECTORY) on it
# would cause a fatal error, even though it would be a no-op.
if(NOT EXISTS "/home/pager/Documents/DeathStarBench/socialNetwork/downloads/libmemcached")
  file(MAKE_DIRECTORY "/home/pager/Documents/DeathStarBench/socialNetwork/downloads/libmemcached")
endif()
file(MAKE_DIRECTORY
  "/home/pager/Documents/DeathStarBench/socialNetwork/build-libmemcached"
  "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix"
  "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix/tmp"
  "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix/src/generate-libmemcached-stamp"
  "/home/pager/Documents/DeathStarBench/socialNetwork/downloads"
  "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix/src/generate-libmemcached-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix/src/generate-libmemcached-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/pager/Documents/DeathStarBench/socialNetwork/src/generate-libmemcached-prefix/src/generate-libmemcached-stamp${cfgdir}") # cfgdir has leading slash
endif()
