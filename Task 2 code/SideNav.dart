import 'package:material/material.dart';
import 'package:adobe_xd/pinned.dart';
import './MOVOptions.dart';
import 'package:adobe_xd/page_link.dart';
import './SUBOptions.dart';
import './XOROptions.dart';
import './DIVOptions.dart';
import './ANDOptions.dart';
import './ADDOptions.dart';
import './INCOptions.dart';
import './SHROptions.dart';
import './CDQOptions.dart';
import './OROptions.dart';
import './MULOptions.dart';
import './DECOptions.dart';
import './SHLOptions.dart';
import './NOTOptions.dart';

class SideNav extends StatelessWidget {
  SideNav({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
          Pinned.fromPins(
            Pin(size: 636.0, end: 0.0),
            Pin(start: 201.0, end: 0.0),
            child: Container(
              decoration: BoxDecoration(
                color: const Color(0xfffa6969),
                boxShadow: [
                  BoxShadow(
                    color: const Color(0x29000000),
                    offset: Offset(0, 3),
                    blurRadius: 6,
                  ),
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 462.0, end: 130.0),
            Pin(size: 84.0, start: 255.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => MOVOptions(),
                ),
              ],
              child: Text(
                'SIMULATE MOV',
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
          Pinned.fromPins(
            Pin(size: 444.0, end: 148.0),
            Pin(size: 84.0, middle: 0.4889),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SUBOptions(),
                ),
              ],
              child: Text(
                'SIMULATE SUB',
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
          Pinned.fromPins(
            Pin(size: 448.0, end: 144.0),
            Pin(size: 84.0, end: 306.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => XOROptions(),
                ),
              ],
              child: Text(
                'SIMULATE XOR',
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
          Align(
            alignment: Alignment(0.492, -0.399),
            child: SizedBox(
              width: 426.0,
              height: 84.0,
              child: PageLink(
                links: [
                  PageLinkInfo(
                    transition: LinkTransition.SlideRight,
                    ease: Curves.easeOut,
                    duration: 0.3,
                    pageBuilder: () => DIVOptions(),
                  ),
                ],
                child: Text(
                  'SIMULATE DIV',
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
          ),
          Pinned.fromPins(
            Pin(size: 456.0, end: 136.0),
            Pin(size: 84.0, middle: 0.676),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => ANDOptions(),
                ),
              ],
              child: Text(
                'SIMULATE AND',
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
          Pinned.fromPins(
            Pin(size: 456.0, end: 130.0),
            Pin(size: 84.0, middle: 0.1755),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideRight,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => ADDOptions(),
                ),
              ],
              child: Text(
                'SIMULATE ADD',
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
          Align(
            alignment: Alignment(0.483, 0.102),
            child: SizedBox(
              width: 422.0,
              height: 84.0,
              child: PageLink(
                links: [
                  PageLinkInfo(
                    transition: LinkTransition.SlideLeft,
                    ease: Curves.easeOut,
                    duration: 0.3,
                    pageBuilder: () => INCOptions(),
                  ),
                ],
                child: Text(
                  'SIMULATE INC',
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
          ),
          Pinned.fromPins(
            Pin(size: 446.0, end: 146.0),
            Pin(size: 84.0, end: 164.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SHROptions(),
                ),
              ],
              child: Text(
                'SIMULATE SHR',
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
          Pinned.fromPins(
            Pin(size: 454.0, end: 138.0),
            Pin(size: 84.0, middle: 0.363),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => CDQOptions(),
                ),
              ],
              child: Text(
                'SIMULATE CDQ',
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
          Align(
            alignment: Alignment(0.452, 0.476),
            child: SizedBox(
              width: 408.0,
              height: 84.0,
              child: PageLink(
                links: [
                  PageLinkInfo(
                    transition: LinkTransition.SlideLeft,
                    ease: Curves.easeOut,
                    duration: 0.3,
                    pageBuilder: () => OROptions(),
                  ),
                ],
                child: Text(
                  'SIMULATE OR',
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
          ),
          Pinned.fromPins(
            Pin(size: 450.0, end: 142.0),
            Pin(size: 84.0, middle: 0.238),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => MULOptions(),
                ),
              ],
              child: Text(
                'SIMULATE MUL',
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
          Pinned.fromPins(
            Pin(size: 442.0, end: 150.0),
            Pin(size: 84.0, middle: 0.6139),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => DECOptions(),
                ),
              ],
              child: Text(
                'SIMULATE DEC',
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
          Pinned.fromPins(
            Pin(size: 438.0, end: 154.0),
            Pin(size: 84.0, end: 23.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SHLOptions(),
                ),
              ],
              child: Text(
                'SIMULATE SHL',
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
          Pinned.fromPins(
            Pin(size: 492.0, end: 100.0),
            Pin(size: 84.0, middle: 0.4255),
            child: Text(
              'SIMULATE XCHG',
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
          Pinned.fromPins(
            Pin(size: 448.0, end: 144.0),
            Pin(size: 84.0, middle: 0.8019),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => NOTOptions(),
                ),
              ],
              child: Text(
                'SIMULATE NOT',
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
    );
  }
}
