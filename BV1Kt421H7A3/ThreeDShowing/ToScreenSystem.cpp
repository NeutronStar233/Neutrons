#include <QMatrix4x4>
#include <QPoint>
#include <iostream>
using namespace std;

pair<QPoint,bool> toScreen(QVector3D P,QMatrix4x4 CameraToWorld,int w,int h)
{
    pair<QPoint,bool> result = pair<QPoint,bool>(QPoint(),true);
    QMatrix4x4 World2Camera = CameraToWorld.inverted();
    QVector3D P_ = World2Camera.map(P);
    if(P_.z()>0)
        result.second = false;
    result.first.setX((200*P_.x()/P_.z())+(w/2));
    result.first.setY((200*P_.y()/P_.z())+(h/2));
    return result;
}
