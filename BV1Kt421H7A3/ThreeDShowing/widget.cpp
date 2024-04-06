#include "widget.h"
#include "ui_widget.h"

#include "ToScreenSystem.cpp"

#include <QPainter>
#include <qdebug.h>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    cw = QVector3D(2,2,3);
}

void Widget::keyPressEvent(QKeyEvent* e)
{
    if(e->key() == Qt::Key_W)
        cw.setX(cw.x()+1);
    if(e->key() == Qt::Key_S)
        cw.setX(cw.x()-1);
    update();
    qDebug()<<"KeyDown";
}

Widget::~Widget()
{
    delete ui;
}

void Widget::mousePressEvent(QMouseEvent* e)
{
    l = e->pos();
}
void Widget::mouseMoveEvent(QMouseEvent* e)
{
    psi += double(e->pos().x()-l.x());
    phi += double(e->pos().y()-l.y());
    l = e->pos();
    update();
}
void Widget::paintEvent(QPaintEvent*)
{
    QPainter pt(this);
    QMatrix4x4 c;
    c.setColumn(3,QVector4D(cw.x(),cw.y(),cw.z(),1));
    c.rotate(psi,QVector3D(0,1,0));
    c.rotate(phi,QVector3D(1,0,0));
    pt.setPen(QPen(Qt::red));
    if(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).second&&toScreen(QVector3D(1,0,0),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).first,toScreen(QVector3D(1,0,0),c,this->width(),this->height()).first);
    pt.setPen(QPen(Qt::blue));
    if(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).second&&toScreen(QVector3D(0,1,0),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).first,toScreen(QVector3D(0,1,0),c,this->width(),this->height()).first);
    pt.setPen(QPen(Qt::green));
    if(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).second&&toScreen(QVector3D(0,0,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,0,0),c,this->width(),this->height()).first,toScreen(QVector3D(0,0,1),c,this->width(),this->height()).first);
    pt.setPen(QPen(Qt::white));

    if(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).second&&toScreen(QVector3D(1,1,0),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).first,toScreen(QVector3D(1,1,0),c,this->width(),this->height()).first);
    if(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).second&&toScreen(QVector3D(0,1,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).first,toScreen(QVector3D(0,1,1),c,this->width(),this->height()).first);
    if(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).second&&toScreen(QVector3D(1,0,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(1,1,1),c,this->width(),this->height()).first,toScreen(QVector3D(1,0,1),c,this->width(),this->height()).first);

    if(toScreen(QVector3D(0,0,1),c,this->width(),this->height()).second&&toScreen(QVector3D(0,1,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,0,1),c,this->width(),this->height()).first,toScreen(QVector3D(0,1,1),c,this->width(),this->height()).first);
    if(toScreen(QVector3D(0,0,1),c,this->width(),this->height()).second&&toScreen(QVector3D(1,0,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,0,1),c,this->width(),this->height()).first,toScreen(QVector3D(1,0,1),c,this->width(),this->height()).first);

    if(toScreen(QVector3D(1,0,0),c,this->width(),this->height()).second&&toScreen(QVector3D(1,0,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(1,0,0),c,this->width(),this->height()).first,toScreen(QVector3D(1,0,1),c,this->width(),this->height()).first);
    if(toScreen(QVector3D(1,0,0),c,this->width(),this->height()).second&&toScreen(QVector3D(1,1,0),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(1,0,0),c,this->width(),this->height()).first,toScreen(QVector3D(1,1,0),c,this->width(),this->height()).first);

    if(toScreen(QVector3D(0,1,0),c,this->width(),this->height()).second&&toScreen(QVector3D(0,1,1),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,1,0),c,this->width(),this->height()).first,toScreen(QVector3D(0,1,1),c,this->width(),this->height()).first);
    if(toScreen(QVector3D(0,1,0),c,this->width(),this->height()).second&&toScreen(QVector3D(1,1,0),c,this->width(),this->height()).second)
    pt.drawLine(toScreen(QVector3D(0,1,0),c,this->width(),this->height()).first,toScreen(QVector3D(1,1,0),c,this->width(),this->height()).first);
}
