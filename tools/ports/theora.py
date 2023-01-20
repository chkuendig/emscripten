# Copyright 2015 The Emscripten Authors.  All rights reserved.
# Emscripten is available under two separate licenses, the MIT license and the
# University of Illinois/NCSA Open Source License.  Both these licenses can be
# found in the LICENSE file.

import logging
import os

VERSION = '1.1.1'
HASH = '9b29764c24c3e966d6935cc017d66fadacc1d2460caa23ba22f5a46940ee050213877f7ce484149c390a1dacde2dd5c48bf081782acfd03e71e2b2ec12a28379'

deps = ['ogg']


def needed(settings):
  return settings.USE_THEORA


def get(ports, settings, shared):

  ports.fetch_project('theora', f'https://github.com/xiph/theora/archive/refs/tags/v{VERSION}.zip', sha512hash=HASH)

  def create(final):
    logging.info('building port: theora')
    source_path = os.path.join(ports.get_dir(), 'theora', 'theora-' + VERSION)
    ports.write_file(os.path.join(source_path, 'config.h'), config_h)
    ports.install_header_dir(os.path.join(source_path, 'include', 'theora'))
    ports.build_port(os.path.join(source_path, 'lib'), final, 'theora',
                     flags=['-sUSE_OGG','-Wno-shift-op-parentheses','-Wno-shift-negative-value','-Wno-parentheses'],
                     exclude_files=[])

  return [shared.cache.get_lib('libtheora.a', create)]


def clear(ports, settings, shared):
  shared.cache.erase_lib('libtheora.a')


def process_dependencies(settings):
  settings.USE_OGG = 1


def process_args(ports):
  return []


def show():
  return 'theora (-sUSE_THEORA; zlib license)'




config_h = '''\
/* config.h.  Generated from config.h.in by configure.  */
/* config.h.in.  Generated from configure.ac by autoheader.  */

/* libcairo is available for visual debugging output */
/* #undef HAVE_CAIRO */

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Define to 1 if you have the <machine/soundcard.h> header file. */
/* #undef HAVE_MACHINE_SOUNDCARD_H */

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* Define to 1 if you have the <soundcard.h> header file. */
/* #undef HAVE_SOUNDCARD_H */

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the <sys/soundcard.h> header file. */
/* #undef HAVE_SYS_SOUNDCARD_H */

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define to the sub-directory in which libtool stores uninstalled libraries.
   */
#define LT_OBJDIR ".libs/"

/* Define to 1 if your C compiler doesn't accept -c and -o together. */
/* #undef NO_MINUS_C_MINUS_O */

/* make use of x86_64 asm optimization */
/* #undef OC_X86_64_ASM */

/* make use of x86 asm optimization */
/* #undef OC_X86_ASM */

/* Name of package */
#define PACKAGE "libtheora"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT ""

/* Define to the full name of this package. */
#define PACKAGE_NAME "libtheora"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "libtheora 1.1.1"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "libtheora"

/* Define to the version of this package. */
#define PACKAGE_VERSION "1.1.1"

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* Define to exclude encode support from the build */
/* #undef THEORA_DISABLE_ENCODE */

/* Define to exclude floating point code from the build */
/* #undef THEORA_DISABLE_FLOAT */

/* Version number of package */
#define VERSION "1.1.1"
'''
