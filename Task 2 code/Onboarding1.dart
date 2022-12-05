import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import './Component11.dart';
import './Onboarding2.dart';
import 'package:adobe_xd/page_link.dart';
import './HomeScreen.dart';
import './Onboarding3.dart';

class Onboarding1 extends StatelessWidget {
  Onboarding1({
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
            Pin(start: 67.0, end: 67.0),
            Pin(size: 254.0, middle: 0.5),
            child: Text(
              'WELCOME TO  OUR 8086/8088 SIMULATOR',
              style: TextStyle(
                fontFamily: 'Carter One',
                fontSize: 82,
                color: const Color(0xffffffff),
              ),
              textAlign: TextAlign.center,
              softWrap: false,
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
            Pin(size: 493.0, start: 20.0),
            Pin(size: 176.0, start: 13.0),
            child: Component11(),
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
                  pageBuilder: () => Onboarding2(),
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
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0xfffa6969),
                borderRadius:
                    BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 40.0, middle: 0.5),
            Pin(size: 40.0, end: 68.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
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
        ],
      ),
    );
  }
}
