#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Simple test for funcube
# Author: Riyas
# Description: Test the Funcube pro with wide band fm BC-Riyas
# Generated: Wed Dec 25 12:52:48 2013
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fcd
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class funcube_fm_broadcast(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Simple test for funcube")
		_icon_path = "/home/risu/.local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 192000

		##################################################
		# Blocks
		##################################################
		self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
			self.GetWin(),
			baseband_freq=0,
			dynamic_range=100,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=512,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Waterfall Plot",
		)
		self.Add(self.wxgui_waterfallsink2_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.fcd_source_c_0 = fcd.source_c("hw:1")
		self.fcd_source_c_0.set_freq(145500000)
		    
		self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/risu/Desktop/fcd_capture_sample.raw")
		self.blocks_file_sink_0.set_unbuffered(False)
		self.blks2_wfm_rcv_0 = blks2.wfm_rcv(
			quad_rate=192000,
			audio_decimation=4,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.fcd_source_c_0, 0), (self.blks2_wfm_rcv_0, 0))
		self.connect((self.blks2_wfm_rcv_0, 0), (self.audio_sink_0, 0))
		self.connect((self.fcd_source_c_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.fcd_source_c_0, 0), (self.blocks_file_sink_0, 0))
		self.connect((self.fcd_source_c_0, 0), (self.wxgui_waterfallsink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = funcube_fm_broadcast()
	tb.Run(True)

