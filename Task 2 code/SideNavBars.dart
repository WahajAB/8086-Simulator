import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import 'package:flutter_svg/flutter_svg.dart';

class SideNavBars extends StatelessWidget {
  SideNavBars({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Pinned.fromPins(
          Pin(start: 0.0, end: 0.0),
          Pin(size: 1.0, start: 0.0),
          child: SvgPicture.string(
            _svg_gy9x9u,
            allowDrawingOutsideViewBox: true,
            fit: BoxFit.fill,
          ),
        ),
        Pinned.fromPins(
          Pin(start: 0.0, end: 0.0),
          Pin(size: 1.0, middle: 0.5102),
          child: SvgPicture.string(
            _svg_qpjiyo,
            allowDrawingOutsideViewBox: true,
            fit: BoxFit.fill,
          ),
        ),
        Pinned.fromPins(
          Pin(start: 0.0, end: 0.0),
          Pin(size: 1.0, end: -1.0),
          child: SvgPicture.string(
            _svg_uer4,
            allowDrawingOutsideViewBox: true,
            fit: BoxFit.fill,
          ),
        ),
      ],
    );
  }
}

const String _svg_gy9x9u =
    '<svg viewBox="0.0 0.0 78.0 1.0" ><path  d="M 78 0 L 0 0" fill="none" stroke="#fa6969" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_qpjiyo =
    '<svg viewBox="0.0 25.0 78.0 1.0" ><path transform="translate(0.0, 25.0)" d="M 78 0 L 0 0" fill="none" stroke="#fa6969" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_uer4 =
    '<svg viewBox="0.0 50.0 78.0 1.0" ><path transform="translate(0.0, 50.0)" d="M 78 0 L 0 0" fill="none" stroke="#fa6969" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
