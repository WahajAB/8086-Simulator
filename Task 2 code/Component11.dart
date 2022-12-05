import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';

class Component11 extends StatelessWidget {
  Component11({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Pinned.fromPins(
          Pin(size: 268.0, end: 49.0),
          Pin(size: 54.0, middle: 0.5),
          child: Text(
            'deez simulators',
            style: TextStyle(
              fontFamily: 'Acme',
              fontSize: 43,
              color: const Color(0xffffffff),
            ),
            textAlign: TextAlign.center,
            softWrap: false,
          ),
        ),
        Pinned.fromPins(
          Pin(size: 176.0, start: 0.0),
          Pin(start: 0.0, end: 0.0),
          child: Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: const AssetImage(''),
                fit: BoxFit.fill,
              ),
            ),
          ),
        ),
        Align(
          alignment: Alignment(1.0, -0.38),
          child: SizedBox(
            width: 34.0,
            height: 34.0,
            child: Stack(
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(5.0),
                  child: SizedBox.expand(
                      child: Text(
                    'TM',
                    style: TextStyle(
                      fontFamily: 'Acme',
                      fontSize: 19,
                      color: const Color(0xffffffff),
                    ),
                    textAlign: TextAlign.center,
                    softWrap: false,
                  )),
                ),
                Container(
                  decoration: BoxDecoration(
                    borderRadius:
                        BorderRadius.all(Radius.elliptical(9999.0, 9999.0)),
                    border:
                        Border.all(width: 1.0, color: const Color(0xffffffff)),
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
