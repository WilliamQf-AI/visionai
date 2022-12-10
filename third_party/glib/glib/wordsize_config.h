// Setup GLib configuration

#ifndef GLIB_GLIB_WORDSIZE_CONFIG_H_
#define GLIB_GLIB_WORDSIZE_CONFIG_H_


#define THIRD_PARTY_GLIB_INT64_TYPE long
#define THIRD_PARTY_GLIB_LONG_SIZE 8
#define THIRD_PARTY_GLIB_LONG_TO_LE GINT64_TO_LE
#define THIRD_PARTY_GLIB_LONG_TO_BE GINT64_TO_BE
#define THIRD_PARTY_GLIB_ULONG_TO_LE GUINT64_TO_LE
#define THIRD_PARTY_GLIB_ULONG_TO_BE GUINT64_TO_BE
#define THIRD_PARTY_GLIB_64_PREFIX "l"
#define THIRD_PARTY_GLIB_SIZE_SIZE 8
#define THIRD_PARTY_GLIB_SIZE_TYPE long
#define THIRD_PARTY_GLIB_SIZE_MAX G_MAXULONG
#define THIRD_PARTY_GLIB_SSIZE_MIN G_MINLONG
#define THIRD_PARTY_GLIB_SSIZE_MAX G_MAXLONG
#define THIRD_PARTY_GLIB_SIZE_PREFIX "l"

#endif  // GLIB_GLIB_WORDSIZE_CONFIG_H_