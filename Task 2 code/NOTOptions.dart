import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import './Component11.dart';
import './SideNavBars.dart';
import './NOTREG.dart';
import 'package:adobe_xd/page_link.dart';
import './HomeScreen.dart';
import 'package:flutter_svg/flutter_svg.dart';

class NOTOptions extends StatelessWidget {
  NOTOptions({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xffcccbcb),
      body: Stack(
        children: <Widget>[
          Stack(
            children: <Widget>[
              Container(
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: const AssetImage(''),
                    fit: BoxFit.fill,
                  ),
                ),
                margin: EdgeInsets.fromLTRB(-1496.0, 0.0, -1584.0, 0.0),
              ),
              Container(
                decoration: BoxDecoration(
                  color: const Color(0xffffffff),
                  border:
                      Border.all(width: 1.0, color: const Color(0xff707070)),
                ),
              ),
            ],
          ),
          Pinned.fromPins(
            Pin(start: 0.0, end: 0.0),
            Pin(size: 201.0, start: 0.0),
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0x33ffffff),
                border: Border.all(width: 1.0, color: const Color(0x33707070)),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 493.0, start: 20.0),
            Pin(size: 176.0, start: 13.0),
            child: Component11(),
          ),
          Pinned.fromPins(
            Pin(size: 78.0, end: 31.5),
            Pin(size: 50.0, start: 75.5),
            child: SideNavBars(),
          ),
          Pinned.fromPins(
            Pin(start: 108.0, end: 108.0),
            Pin(size: 208.0, middle: 0.5),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => NOTREG(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(104.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.003, 0.0),
                    child: SizedBox(
                      width: 124.0,
                      height: 84.0,
                      child: Text(
                        'REG',
                        style: TextStyle(
                          fontFamily: 'Nunito',
                          fontSize: 61,
                          color: const Color(0xffffffff),
                          fontWeight: FontWeight.w700,
                        ),
                        textAlign: TextAlign.center,
                        softWrap: false,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 215.0, start: 7.0),
            Pin(size: 102.0, start: 244.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideRight,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => HomeScreen(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(51.0),
                      border: Border.all(
                          width: 4.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Pinned.fromPins(
                    Pin(size: 94.0, end: 25.0),
                    Pin(size: 46.0, middle: 0.5179),
                    child: Text(
                      'BACK',
                      style: TextStyle(
                        fontFamily: 'Nunito',
                        fontSize: 34,
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w700,
                      ),
                      textAlign: TextAlign.center,
                      softWrap: false,
                    ),
                  ),
                  Pinned.fromPins(
                    Pin(size: 63.0, start: 25.0),
                    Pin(start: 20.0, end: 19.0),
                    child: Container(
                      decoration: BoxDecoration(
                        color: const Color(0xfffa6969),
                        borderRadius:
                            BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
                      ),
                    ),
                  ),
                  Align(
                    alignment: Alignment(-0.548, 0.015),
                    child: SizedBox(
                      width: 18.0,
                      height: 36.0,
                      child: Stack(
                        children: <Widget>[
                          Pinned.fromPins(
                            Pin(start: 0.0, end: 0.0),
                            Pin(size: 18.0, start: 0.0),
                            child: SvgPicture.string(
                              _svg_dk6fvs,
                              allowDrawingOutsideViewBox: true,
                              fit: BoxFit.fill,
                            ),
                          ),
                          Pinned.fromPins(
                            Pin(start: 0.0, end: 0.0),
                            Pin(size: 18.0, end: 0.0),
                            child: SvgPicture.string(
                              _svg_ajbk0,
                              allowDrawingOutsideViewBox: true,
                              fit: BoxFit.fill,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

const String _svg_dk6fvs =
    '<svg viewBox="26.5 274.5 18.0 18.0" ><path transform="translate(26.5, 274.5)" d="M 0 18 L 18 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_ajbk0 =
    '<svg viewBox="26.5 292.5 18.0 18.0" ><path transform="translate(26.5, 292.5)" d="M 18 18 L 0 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
