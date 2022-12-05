import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import './HomeScreen.dart';
import 'package:adobe_xd/page_link.dart';
import './Onboarding1.dart';
import './Onboarding2.dart';
import './Component11.dart';
import 'package:flutter_svg/flutter_svg.dart';

class Onboarding3 extends StatelessWidget {
  Onboarding3({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xffffffff),
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
            Pin(start: -67.0, end: -68.0),
            Pin(size: 1152.0, middle: 0.5),
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0xfffa6969),
                borderRadius: BorderRadius.circular(576.0),
                border: Border.all(width: 8.0, color: const Color(0xfffa6969)),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(0.0, 189.0, 0.0, 0.0),
            child: SizedBox.expand(
                child: SvgPicture.string(
              _svg_t2i02p,
              allowDrawingOutsideViewBox: true,
              fit: BoxFit.fill,
            )),
          ),
          Align(
            alignment: Alignment(-0.558, -0.169),
            child: SizedBox(
              width: 133.0,
              height: 1.0,
              child: SvgPicture.string(
                _svg_apfcgp,
                allowDrawingOutsideViewBox: true,
              ),
            ),
          ),
          Align(
            alignment: Alignment(-0.558, -0.136),
            child: SizedBox(
              width: 133.0,
              height: 1.0,
              child: SvgPicture.string(
                _svg_uqj3v,
                allowDrawingOutsideViewBox: true,
              ),
            ),
          ),
          Align(
            alignment: Alignment(-0.558, -0.103),
            child: SizedBox(
              width: 133.0,
              height: 1.0,
              child: SvgPicture.string(
                _svg_ko4951,
                allowDrawingOutsideViewBox: true,
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 728.0, end: 76.0),
            Pin(size: 164.0, middle: 0.5726),
            child: Text(
              'click on this iconto view the list of commands',
              style: TextStyle(
                fontFamily: 'Acme',
                fontSize: 65,
                color: const Color(0xffffffff),
              ),
              textAlign: TextAlign.center,
              softWrap: false,
            ),
          ),
          Align(
            alignment: Alignment(-0.469, 0.013),
            child: SizedBox(
              width: 38.0,
              height: 124.0,
              child: Stack(
                children: <Widget>[
                  Align(
                    alignment: Alignment.topLeft,
                    child: SizedBox(
                      width: 19.0,
                      height: 36.0,
                      child: SvgPicture.string(
                        _svg_xeiudi,
                        allowDrawingOutsideViewBox: true,
                      ),
                    ),
                  ),
                  Align(
                    alignment: Alignment.topRight,
                    child: SizedBox(
                      width: 19.0,
                      height: 36.0,
                      child: SvgPicture.string(
                        _svg_bfsi,
                        allowDrawingOutsideViewBox: true,
                      ),
                    ),
                  ),
                  Pinned.fromPins(
                    Pin(size: 1.0, middle: 0.5135),
                    Pin(start: 0.0, end: 0.0),
                    child: SvgPicture.string(
                      _svg_xcbiw9,
                      allowDrawingOutsideViewBox: true,
                      fit: BoxFit.fill,
                    ),
                  ),
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 146.0, end: 91.0),
            Pin(size: 63.0, end: 57.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => HomeScreen(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  SizedBox.expand(
                      child: Text(
                    'FINISH',
                    style: TextStyle(
                      fontFamily: 'Acme',
                      fontSize: 50,
                      color: const Color(0xffffffff),
                    ),
                    textAlign: TextAlign.center,
                    softWrap: false,
                  )),
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 40.0, middle: 0.4385),
            Pin(size: 40.0, end: 68.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideRight,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => Onboarding1(),
                ),
              ],
              child: Container(
                decoration: BoxDecoration(
                  borderRadius:
                      BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
                  border:
                      Border.all(width: 1.0, color: const Color(0xfffa6969)),
                ),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 40.0, middle: 0.5),
            Pin(size: 40.0, end: 68.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideRight,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => Onboarding2(),
                ),
              ],
              child: Container(
                decoration: BoxDecoration(
                  borderRadius:
                      BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
                  border:
                      Border.all(width: 1.0, color: const Color(0xfffa6969)),
                ),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 40.0, middle: 0.5615),
            Pin(size: 40.0, end: 68.0),
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0xfffa6969),
                borderRadius:
                    BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 493.0, start: 20.0),
            Pin(size: 176.0, start: 13.0),
            child: Component11(),
          ),
        ],
      ),
    );
  }
}

const String _svg_t2i02p =
    '<svg viewBox="0.0 189.0 1080.0 2151.0" ><path transform="translate(1737.0, -301.0)" d="M -656.9989624023438 2641.0009765625 L -1737 2640.99951171875 L -1737 489.9996032714844 L -657.0000610351562 489.9996032714844 L -657.0000610351562 1599.000366210938 C -657.0018920898438 1593.649291992188 -657.5426635742188 1588.29931640625 -658.6092529296875 1583.099365234375 C -659.6487426757812 1578.031982421875 -661.1995239257812 1573.0458984375 -663.218994140625 1568.279541015625 C -665.2013549804688 1563.60009765625 -667.65478515625 1559.085693359375 -670.5108032226562 1554.861450195312 C -673.3397827148438 1550.677490234375 -676.5879516601562 1546.7421875 -680.1650390625 1543.165161132812 C -683.742431640625 1539.587768554688 -687.6774291992188 1536.339599609375 -691.861328125 1533.510620117188 C -696.0855712890625 1530.654296875 -700.6000366210938 1528.20068359375 -705.2792358398438 1526.21826171875 C -710.0458374023438 1524.198852539062 -715.0318603515625 1522.6474609375 -720.0989990234375 1521.608032226562 C -725.2992553710938 1520.540893554688 -730.6492309570312 1520.000122070312 -736.0003051757812 1520.000122070312 L -1432 1520.000122070312 C -1475.560791015625 1520.000122070312 -1511 1555.439331054688 -1511 1599.000366210938 L -1511 1658.000122070312 C -1511 1701.560668945312 -1475.560791015625 1736.999877929688 -1432 1736.999877929688 L -736.0003051757812 1736.999877929688 C -692.4392700195312 1736.999877929688 -657.0000610351562 1701.560668945312 -657.0000610351562 1658.000122070312 L -657.0000610351562 2641.000732421875 L -656.999267578125 2640.998779296875 L -657.0000610351562 2640.9990234375 L -657.0000610351562 2641.000732421875 L -657.0000610351562 2641.0009765625 L -656.9989624023438 2641.0009765625 Z M -1457 1187.999877929688 C -1525.3740234375 1187.999877929688 -1581.000244140625 1243.626220703125 -1581.000244140625 1312.000122070312 C -1581.000244140625 1380.374389648438 -1525.3740234375 1436.000610351562 -1457 1436.000610351562 C -1388.626098632812 1436.000610351562 -1333 1380.374389648438 -1333 1312.000122070312 C -1333 1243.626220703125 -1388.626098632812 1187.999877929688 -1457 1187.999877929688 Z" fill="#ffffff" stroke="none" stroke-width="1" stroke-miterlimit="4" stroke-linecap="butt" /></svg>';
const String _svg_apfcgp =
    '<svg viewBox="209.5 971.5 133.0 1.0" ><path transform="translate(209.5, 971.5)" d="M 0 0 L 133 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_uqj3v =
    '<svg viewBox="209.5 1010.5 133.0 1.0" ><path transform="translate(209.5, 1010.5)" d="M 0 0 L 133 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_ko4951 =
    '<svg viewBox="209.5 1049.5 133.0 1.0" ><path transform="translate(209.5, 1049.5)" d="M 0 0 L 133 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_xeiudi =
    '<svg viewBox="276.5 1122.5 19.0 36.0" ><path transform="translate(276.5, 1122.5)" d="M 0 36 L 19 0" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_bfsi =
    '<svg viewBox="295.5 1122.5 19.0 36.0" ><path transform="translate(295.5, 1122.5)" d="M 0 0 L 19 36" fill="none" stroke="#ffffff" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
const String _svg_xcbiw9 =
    '<svg viewBox="295.5 1122.5 1.0 124.0" ><path transform="translate(295.5, 1122.5)" d="M 0 0 L 0 124" fill="none" stroke="#fdfdfd" stroke-width="8" stroke-miterlimit="4" stroke-linecap="round" /></svg>';
