import 'package:flutter/material.dart';
import 'package:adobe_xd/pinned.dart';

class ORREGTOREG extends StatelessWidget {
  ORREGTOREG({
    Key key,
  }) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
          Align(
            alignment: Alignment(-0.329, 0.104),
            child: SizedBox(
              width: 227.0,
              height: 55.0,
              child: Stack(
                children: <Widget>[
                  Container(
                    color: const Color(0xff032a29),
                  ),
                  Pinned.fromPins(
                    Pin(size: 143.0, middle: 0.4524),
                    Pin(start: 7.0, end: 7.0),
                    child: Text(
                      'OR AX,BX',
                      style: TextStyle(
                        fontFamily: 'Nunito',
                        fontSize: 30,
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w700,
                      ),
                      softWrap: false,
                    ),
                  ),
                ],
              ),
            ),
          ),
          Align(
            alignment: Alignment(-0.51, 0.435),
            child: SizedBox(
              width: 227.0,
              height: 55.0,
              child: Stack(
                children: <Widget>[
                  Container(
                    color: const Color(0xff032a29),
                  ),
                  Pinned.fromPins(
                    Pin(size: 143.0, middle: 0.5),
                    Pin(start: 7.0, end: 7.0),
                    child: Text(
                      'OR AX,BX',
                      style: TextStyle(
                        fontFamily: 'Nunito',
                        fontSize: 30,
                        color: const Color(0xffffffff),
                        fontWeight: FontWeight.w700,
                      ),
                      softWrap: false,
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
