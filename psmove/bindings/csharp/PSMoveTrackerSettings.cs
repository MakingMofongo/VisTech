//------------------------------------------------------------------------------
// <auto-generated />
//
// This file was automatically generated by SWIG (http://www.swig.org).
// Version 3.0.12
//
// Do not make changes to this file unless you know what you are doing--modify
// the SWIG interface file instead.
//------------------------------------------------------------------------------

namespace io.thp.psmove {

public class PSMoveTrackerSettings : global::System.IDisposable {
  private global::System.Runtime.InteropServices.HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal PSMoveTrackerSettings(global::System.IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new global::System.Runtime.InteropServices.HandleRef(this, cPtr);
  }

  internal static global::System.Runtime.InteropServices.HandleRef getCPtr(PSMoveTrackerSettings obj) {
    return (obj == null) ? new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero) : obj.swigCPtr;
  }

  ~PSMoveTrackerSettings() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          psmoveapi_csharpPINVOKE.delete_PSMoveTrackerSettings(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
      global::System.GC.SuppressFinalize(this);
    }
  }

  public int camera_frame_width {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_width_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_width_get(swigCPtr);
      return ret;
    } 
  }

  public int camera_frame_height {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_height_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_height_get(swigCPtr);
      return ret;
    } 
  }

  public int camera_frame_rate {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_rate_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_frame_rate_get(swigCPtr);
      return ret;
    } 
  }

  public PSMove_Bool camera_auto_gain {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_auto_gain_set(swigCPtr, (int)value);
    } 
    get {
      PSMove_Bool ret = (PSMove_Bool)psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_auto_gain_get(swigCPtr);
      return ret;
    } 
  }

  public int camera_gain {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_gain_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_gain_get(swigCPtr);
      return ret;
    } 
  }

  public PSMove_Bool camera_auto_white_balance {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_auto_white_balance_set(swigCPtr, (int)value);
    } 
    get {
      PSMove_Bool ret = (PSMove_Bool)psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_auto_white_balance_get(swigCPtr);
      return ret;
    } 
  }

  public int camera_exposure {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_exposure_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_exposure_get(swigCPtr);
      return ret;
    } 
  }

  public int camera_brightness {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_brightness_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_brightness_get(swigCPtr);
      return ret;
    } 
  }

  public PSMove_Bool camera_mirror {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_mirror_set(swigCPtr, (int)value);
    } 
    get {
      PSMove_Bool ret = (PSMove_Bool)psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_camera_mirror_get(swigCPtr);
      return ret;
    } 
  }

  public Exposure exposure_mode {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_exposure_mode_set(swigCPtr, (int)value);
    } 
    get {
      Exposure ret = (Exposure)psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_exposure_mode_get(swigCPtr);
      return ret;
    } 
  }

  public int calibration_blink_delay {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_blink_delay_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_blink_delay_get(swigCPtr);
      return ret;
    } 
  }

  public int calibration_diff_t {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_diff_t_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_diff_t_get(swigCPtr);
      return ret;
    } 
  }

  public int calibration_min_size {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_min_size_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_min_size_get(swigCPtr);
      return ret;
    } 
  }

  public int calibration_max_distance {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_max_distance_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_max_distance_get(swigCPtr);
      return ret;
    } 
  }

  public int calibration_size_std {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_size_std_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_calibration_size_std_get(swigCPtr);
      return ret;
    } 
  }

  public int color_mapping_max_age {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_mapping_max_age_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_mapping_max_age_get(swigCPtr);
      return ret;
    } 
  }

  public float dimming_factor {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_dimming_factor_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_dimming_factor_get(swigCPtr);
      return ret;
    } 
  }

  public int color_hue_filter_range {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_hue_filter_range_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_hue_filter_range_get(swigCPtr);
      return ret;
    } 
  }

  public int color_saturation_filter_range {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_saturation_filter_range_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_saturation_filter_range_get(swigCPtr);
      return ret;
    } 
  }

  public int color_value_filter_range {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_value_filter_range_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_value_filter_range_get(swigCPtr);
      return ret;
    } 
  }

  public int tracker_adaptive_xy {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_adaptive_xy_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_adaptive_xy_get(swigCPtr);
      return ret;
    } 
  }

  public int tracker_adaptive_z {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_adaptive_z_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_adaptive_z_get(swigCPtr);
      return ret;
    } 
  }

  public float color_adaption_quality_t {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_adaption_quality_t_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_adaption_quality_t_get(swigCPtr);
      return ret;
    } 
  }

  public float color_update_rate {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_rate_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_rate_get(swigCPtr);
      return ret;
    } 
  }

  public int search_tile_width {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tile_width_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tile_width_get(swigCPtr);
      return ret;
    } 
  }

  public int search_tile_height {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tile_height_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tile_height_get(swigCPtr);
      return ret;
    } 
  }

  public int search_tiles_horizontal {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tiles_horizontal_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tiles_horizontal_get(swigCPtr);
      return ret;
    } 
  }

  public int search_tiles_count {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tiles_count_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_search_tiles_count_get(swigCPtr);
      return ret;
    } 
  }

  public int roi_adjust_fps_t {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_roi_adjust_fps_t_set(swigCPtr, value);
    } 
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_roi_adjust_fps_t_get(swigCPtr);
      return ret;
    } 
  }

  public float tracker_quality_t1 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t1_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t1_get(swigCPtr);
      return ret;
    } 
  }

  public float tracker_quality_t2 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t2_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t2_get(swigCPtr);
      return ret;
    } 
  }

  public float tracker_quality_t3 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t3_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_tracker_quality_t3_get(swigCPtr);
      return ret;
    } 
  }

  public float color_update_quality_t1 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t1_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t1_get(swigCPtr);
      return ret;
    } 
  }

  public float color_update_quality_t2 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t2_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t2_get(swigCPtr);
      return ret;
    } 
  }

  public float color_update_quality_t3 {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t3_set(swigCPtr, value);
    } 
    get {
      float ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_color_update_quality_t3_get(swigCPtr);
      return ret;
    } 
  }

  public string intrinsics_xml {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_intrinsics_xml_set(swigCPtr, value);
    } 
    get {
      string ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_intrinsics_xml_get(swigCPtr);
      return ret;
    } 
  }

  public string distortion_xml {
    set {
      psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_distortion_xml_set(swigCPtr, value);
    } 
    get {
      string ret = psmoveapi_csharpPINVOKE.PSMoveTrackerSettings_distortion_xml_get(swigCPtr);
      return ret;
    } 
  }

  public PSMoveTrackerSettings() : this(psmoveapi_csharpPINVOKE.new_PSMoveTrackerSettings(), true) {
  }

}

}
