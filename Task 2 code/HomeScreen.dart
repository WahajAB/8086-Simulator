import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';
import './Component11.dart';
import './SideNavBars.dart';
import './MOVOptions.dart';
import 'package:adobe_xd/page_link.dart';
import './CDQOptions.dart';
import './DECOptions.dart';
import './DIVOptions.dart';
import './ANDOptions.dart';
import './ADDOptions.dart';
import './INCOptions.dart';
import './NOTOptions.dart';
import './SHROptions.dart';
import './SHLOptions.dart';
import './MULOptions.dart';
import './SUBOptions.dart';
import './OROptions.dart';
import './XOROptions.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({
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
            Pin(start: 158.0, end: 157.0),
            Pin(size: 168.0, start: 277.0),
            child: Stack(
              children: <Widget>[
                Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(84.0),
                    border:
                        Border.all(width: 8.0, color: const Color(0xfffa6969)),
                  ),
                ),
                Pinned.fromPins(
                  Pin(start: 83.0, end: 83.0),
                  Pin(size: 80.0, middle: 0.5),
                  child: Text(
                    '8086/8088 SIMULATOR',
                    style: TextStyle(
                      fontFamily: 'Carter One',
                      fontSize: 52,
                      color: const Color(0xffffffff),
                    ),
                    textAlign: TextAlign.center,
                    softWrap: false,
                  ),
                ),
              ],
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
            Pin(size: 78.0, end: 31.5),
            Pin(size: 50.0, start: 75.5),
            child: SideNavBars(),
          ),
          Pinned.fromPins(
            Pin(size: 356.0, start: 136.0),
            Pin(size: 166.0, middle: 0.2682),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => MOVOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 144.0,
                      height: 84.0,
                      child: Text(
                        'MOV',
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
            Pin(size: 356.0, start: 136.0),
            Pin(size: 166.0, middle: 0.4581),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => CDQOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Stack(
                    children: <Widget>[
                      Container(
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(94.0),
                          border: Border.all(
                              width: 8.0, color: const Color(0xfffa6969)),
                        ),
                      ),
                      Center(
                        child: SizedBox(
                          width: 136.0,
                          height: 84.0,
                          child: Text(
                            'CDQ',
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
                ],
              ),
            ),
          ),
          Pinned.fromPins(
            Pin(size: 356.0, start: 136.0),
            Pin(size: 167.0, middle: 0.648),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => DECOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.0, 0.012),
                    child: SizedBox(
                      width: 124.0,
                      height: 84.0,
                      child: Text(
                        'DEC',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 166.0, middle: 0.2682),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => DIVOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 108.0,
                      height: 84.0,
                      child: Text(
                        'DIV',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 166.0, middle: 0.4581),
            child: Stack(
              children: <Widget>[
                Container(
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(94.0),
                    border:
                        Border.all(width: 8.0, color: const Color(0xfffa6969)),
                  ),
                ),
                Center(
                  child: SizedBox(
                    width: 172.0,
                    height: 84.0,
                    child: Text(
                      'XCHG',
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
          Pinned.fromPins(
            Pin(size: 356.0, end: 136.0),
            Pin(size: 167.0, middle: 0.648),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => ANDOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.0, 0.012),
                    child: SizedBox(
                      width: 138.0,
                      height: 84.0,
                      child: Text(
                        'AND',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 167.0, middle: 0.3631),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => ADDOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.0, 0.012),
                    child: SizedBox(
                      width: 138.0,
                      height: 84.0,
                      child: Text(
                        'ADD',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 166.0, middle: 0.5529),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => INCOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 104.0,
                      height: 84.0,
                      child: Text(
                        'INC',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 166.0, middle: 0.7429),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => NOTOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.004, 0.0),
                    child: SizedBox(
                      width: 129.0,
                      height: 84.0,
                      child: Text(
                        'NOT',
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
            Pin(size: 356.0, end: 136.0),
            Pin(size: 166.0, middle: 0.8376),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SHROptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.009, 0.0),
                    child: SizedBox(
                      width: 128.0,
                      height: 84.0,
                      child: Text(
                        'SHR',
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
            Pin(size: 356.0, middle: 0.5),
            Pin(size: 166.0, end: 147.0),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SHLOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 120.0,
                      height: 84.0,
                      child: Text(
                        'SHL',
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
            Pin(size: 356.0, start: 136.0),
            Pin(size: 167.0, middle: 0.3631),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => MULOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Align(
                    alignment: Alignment(0.0, 0.012),
                    child: SizedBox(
                      width: 132.0,
                      height: 84.0,
                      child: Text(
                        'MUL',
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
            Pin(size: 356.0, start: 136.0),
            Pin(size: 166.0, middle: 0.5529),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => SUBOptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 126.0,
                      height: 84.0,
                      child: Text(
                        'SUB',
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
            Pin(size: 356.0, start: 136.0),
            Pin(size: 166.0, middle: 0.7429),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => OROptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 90.0,
                      height: 84.0,
                      child: Text(
                        'OR',
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
            Pin(size: 356.0, start: 136.0),
            Pin(size: 166.0, middle: 0.8376),
            child: PageLink(
              links: [
                PageLinkInfo(
                  transition: LinkTransition.SlideLeft,
                  ease: Curves.easeOut,
                  duration: 0.3,
                  pageBuilder: () => XOROptions(),
                ),
              ],
              child: Stack(
                children: <Widget>[
                  Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(94.0),
                      border: Border.all(
                          width: 8.0, color: const Color(0xfffa6969)),
                    ),
                  ),
                  Center(
                    child: SizedBox(
                      width: 130.0,
                      height: 84.0,
                      child: Text(
                        'XOR',
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
        ],
      ),
    );
  }
}
