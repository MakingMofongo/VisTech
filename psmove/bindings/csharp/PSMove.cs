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

public class PSMove : global::System.IDisposable {
  private global::System.Runtime.InteropServices.HandleRef swigCPtr;
  protected bool swigCMemOwn;

  internal PSMove(global::System.IntPtr cPtr, bool cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = new global::System.Runtime.InteropServices.HandleRef(this, cPtr);
  }

  internal static global::System.Runtime.InteropServices.HandleRef getCPtr(PSMove obj) {
    return (obj == null) ? new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero) : obj.swigCPtr;
  }

  ~PSMove() {
    Dispose();
  }

  public virtual void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != global::System.IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          psmoveapi_csharpPINVOKE.delete_PSMove(swigCPtr);
        }
        swigCPtr = new global::System.Runtime.InteropServices.HandleRef(null, global::System.IntPtr.Zero);
      }
      global::System.GC.SuppressFinalize(this);
    }
  }

  public int connection_type {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_connection_type_get(swigCPtr);
      return ret;
    } 
  }

  public int ax {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_ax_get(swigCPtr);
      return ret;
    } 
  }

  public int ay {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_ay_get(swigCPtr);
      return ret;
    } 
  }

  public int az {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_az_get(swigCPtr);
      return ret;
    } 
  }

  public int gx {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_gx_get(swigCPtr);
      return ret;
    } 
  }

  public int gy {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_gy_get(swigCPtr);
      return ret;
    } 
  }

  public int gz {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_gz_get(swigCPtr);
      return ret;
    } 
  }

  public int mx {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_mx_get(swigCPtr);
      return ret;
    } 
  }

  public int my {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_my_get(swigCPtr);
      return ret;
    } 
  }

  public int mz {
    get {
      int ret = psmoveapi_csharpPINVOKE.PSMove_mz_get(swigCPtr);
      return ret;
    } 
  }

  public PSMove() : this(psmoveapi_csharpPINVOKE.new_PSMove__SWIG_0(), true) {
  }

  public PSMove(int id) : this(psmoveapi_csharpPINVOKE.new_PSMove__SWIG_1(id), true) {
  }

  public void get_accelerometer_frame(Frame frame, out float arg1, out float arg2, out float arg3) {
    psmoveapi_csharpPINVOKE.PSMove_get_accelerometer_frame(swigCPtr, (int)frame, out arg1, out arg2, out arg3);
  }

  public void get_gyroscope_frame(Frame frame, out float arg1, out float arg2, out float arg3) {
    psmoveapi_csharpPINVOKE.PSMove_get_gyroscope_frame(swigCPtr, (int)frame, out arg1, out arg2, out arg3);
  }

  public void get_magnetometer_vector(out float arg0, out float arg1, out float arg2) {
    psmoveapi_csharpPINVOKE.PSMove_get_magnetometer_vector(swigCPtr, out arg0, out arg1, out arg2);
  }

  public void enable_orientation(int enabled) {
    psmoveapi_csharpPINVOKE.PSMove_enable_orientation(swigCPtr, enabled);
  }

  public int has_orientation() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_has_orientation(swigCPtr);
    return ret;
  }

  public int has_calibration() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_has_calibration(swigCPtr);
    return ret;
  }

  public void get_orientation(out float arg0, out float arg1, out float arg2, out float arg3) {
    psmoveapi_csharpPINVOKE.PSMove_get_orientation(swigCPtr, out arg0, out arg1, out arg2, out arg3);
  }

  public void reset_orientation() {
    psmoveapi_csharpPINVOKE.PSMove_reset_orientation(swigCPtr);
  }

  public void set_leds(int r, int g, int b) {
    psmoveapi_csharpPINVOKE.PSMove_set_leds(swigCPtr, r, g, b);
  }

  public void set_rumble(int rumble) {
    psmoveapi_csharpPINVOKE.PSMove_set_rumble(swigCPtr, rumble);
  }

  public int update_leds() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_update_leds(swigCPtr);
    return ret;
  }

  public void set_rate_limiting(int enabled) {
    psmoveapi_csharpPINVOKE.PSMove_set_rate_limiting(swigCPtr, enabled);
  }

  public int pair() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_pair(swigCPtr);
    return ret;
  }

  public int pair_custom(string btaddr) {
    int ret = psmoveapi_csharpPINVOKE.PSMove_pair_custom(swigCPtr, btaddr);
    return ret;
  }

  public string get_serial() {
    string ret = psmoveapi_csharpPINVOKE.PSMove_get_serial(swigCPtr);
    return ret;
  }

  public int is_remote() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_is_remote(swigCPtr);
    return ret;
  }

  public int poll() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_poll(swigCPtr);
    return ret;
  }

  public int get_buttons() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_get_buttons(swigCPtr);
    return ret;
  }

  public void get_button_events(out uint arg0, out uint arg1) {
    psmoveapi_csharpPINVOKE.PSMove_get_button_events(swigCPtr, out arg0, out arg1);
  }

  public int get_battery() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_get_battery(swigCPtr);
    return ret;
  }

  public int get_temperature() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_get_temperature(swigCPtr);
    return ret;
  }

  public float get_temperature_in_celsius() {
    float ret = psmoveapi_csharpPINVOKE.PSMove_get_temperature_in_celsius(swigCPtr);
    return ret;
  }

  public int get_trigger() {
    int ret = psmoveapi_csharpPINVOKE.PSMove_get_trigger(swigCPtr);
    return ret;
  }

}

}
