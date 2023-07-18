/* GStreamer
 *
 * Copyright (C) 2014-2015 Sebastian Dröge <sebastian@centricular.com>
 * Copyright (C) 2015 Brijesh Singh <brijesh.ksingh@gmail.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
 * Boston, MA 02110-1301, USA.
 */

#ifndef __GST_PLAY_VISUALIZATION_H__
#define __GST_PLAY_VISUALIZATION_H__

#include "third_party/gstreamer/subprojects/gstreamer/gst/gst.h"
#include "third_party/gstreamer/subprojects/gst_plugins_bad/gst_libs/gst/play/play-prelude.h"

G_BEGIN_DECLS

typedef struct _GstPlayVisualization GstPlayVisualization;
/**
 * GstPlayVisualization:
 * @name: name of the visualization.
 * @description: description of the visualization.
 *
 * A #GstPlayVisualization descriptor.
 * Since: 1.20
 */
struct _GstPlayVisualization {
  gchar *name;
  gchar *description;
};

GST_PLAY_API
GType                     gst_play_visualization_get_type (void);

GST_PLAY_API
GstPlayVisualization *  gst_play_visualization_copy  (const GstPlayVisualization *vis);

GST_PLAY_API
void                      gst_play_visualization_free  (GstPlayVisualization *vis);

GST_PLAY_API
GstPlayVisualization ** gst_play_visualizations_get  (void);

GST_PLAY_API
void                      gst_play_visualizations_free (GstPlayVisualization **viss);

#ifdef G_DEFINE_AUTOPTR_CLEANUP_FUNC
G_DEFINE_AUTOPTR_CLEANUP_FUNC(GstPlayVisualization, gst_play_visualization_free)
#endif

G_END_DECLS

#endif /* __GST_PLAY_VISUALIZATION_H__ */
