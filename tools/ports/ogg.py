# Copyright 2015 The Emscripten Authors.  All rights reserved.
# Emscripten is available under two separate licenses, the MIT license and the
# University of Illinois/NCSA Open Source License.  Both these licenses can be
# found in the LICENSE file.

import logging
import os

VERSION = '1.3.5'
HASH = 'e7b5f5d469090b66dbb33634591ae6de41af3a5644c10488e59ba7428ed78912e208a2c0fbb5003ec5b7eb2a0102a2f85cecb21fa9512d790139ecc45b6d03f4'


def needed(settings):
  return settings.USE_OGG


def get(ports, settings, shared):
  ports.fetch_project('ogg', f'https://github.com/xiph/ogg/releases/download/v{VERSION}/libogg-{VERSION}.zip', sha512hash=HASH)

  def create(final):
    logging.info('building port: ogg')

    source_path = os.path.join(ports.get_dir(), 'ogg', 'libogg-' + VERSION)
    ports.write_file(os.path.join(source_path, 'include', 'ogg', 'config_types.h'), config_types_h)
    ports.install_header_dir(os.path.join(source_path, 'include', 'ogg'), 'ogg')
    ports.build_port(os.path.join(source_path, 'src'), final, 'ogg')

  return [shared.cache.get_lib('libogg.a', create)]


def clear(ports, settings, shared):
  shared.cache.erase_lib('libogg.a')


def process_args(ports):
  return []


def show():
  return 'ogg (USE_OGG=1; zlib license)'


config_types_h = '''\
#ifndef __CONFIG_TYPES_H__
#define __CONFIG_TYPES_H__

/* these are filled in by configure */
#define INCLUDE_INTTYPES_H 1
#define INCLUDE_STDINT_H 1
#define INCLUDE_SYS_TYPES_H 1

#if INCLUDE_INTTYPES_H
#  include <inttypes.h>
#endif
#if INCLUDE_STDINT_H
#  include <stdint.h>
#endif
#if INCLUDE_SYS_TYPES_H
#  include <sys/types.h>
#endif

typedef int16_t ogg_int16_t;
typedef uint16_t ogg_uint16_t;
typedef int32_t ogg_int32_t;
typedef uint32_t ogg_uint32_t;
typedef int64_t ogg_int64_t;
typedef uint64_t ogg_uint64_t;

#endif
'''
