import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import './Onboarding3.dart';
import 'package:adobe_xd/page_link.dart';
import './HomeScreen.dart';
import './Onboarding1.dart';
import './Component11.dart';

class Onboarding2 extends StatelessWidget {
  Onboarding2({
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
          Align(
            alignment: Alignment(0.07, 0.0),
            child: SizedBox(
              width: 680.0,
              height: 312.0,
              child: Text(
                'Before we begin,let\'s take a quick stepthrought he tutorial!',
                style: TextStyle(
                  fontFamily: 'Acme',
                  fontSize: 82,
                  color: const Color(0xffffffff),
                ),
                textAlign: TextAlign.center,
                softWrap: false,
              ),
            ),
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
            Pin(size: 114.0, start: 85.0),
            Pin(size: 63.0, end: 57.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => Onboarding3(),
                ),
              ],
              child: Text(
                'NEXT',
                style: TextStyle(
                  fontFamily: 'Acme',
                  fontSize: 50,
                  color: const Color(0xffffffff),
                ),
                textAlign: TextAlign.center,
                softWrap: false,
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 94.0, end: 117.0),
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
              child: Text(
                'SKIP',
                style: TextStyle(
                  fontFamily: 'Acme',
                  fontSize: 50,
                  color: const Color(0xffffffff),
                ),
                textAlign: TextAlign.center,
                softWrap: false,
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
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0xfffa6969),
                borderRadius:
                    BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 40.0, middle: 0.5615),
            Pin(size: 40.0, end: 68.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => Onboarding3(),
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
            Pin(size: 493.0, start: 20.0),
            Pin(size: 176.0, start: 13.0),
            child: Component11(),
          ),
        ],
      ),
    );
  }
}
