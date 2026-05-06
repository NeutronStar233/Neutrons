from NTools import *
#NeutronStar233
class s1(NScene):
    def construct(self):
        l = Line(LEFT*8+DOWN,RIGHT*8+DOWN,color=BLACK)
        A = Dot(UP*0.5,color=BLACK)
        t_A = MathTex("A",color=BLACK).next_to(A,UP)
        self.say(["设这就是给定的直线",
                  "且其外一点为A"],
                 Create(l),FadeIn(A,t_A))

        c_A = Circle(radius=1.618*1.5,color=BLACK).move_to(A.get_center())
        B = Dot(cross_cl(c_A,l)[1],color=BLACK)
        t_B = MathTex("B",color=BLACK).next_to(B,LEFT)
        self.say(["以A为圆心作圆A",
                  "使之交给定直线于两点",
                  "设B为其中一点"],
                 Create(c_A),FadeIn(B,t_B))

        c_B = Circle(radius=distance(A,B),color=BLACK).move_to(B.get_center())
        C = Dot(cross_c(c_B,c_A)[1],color=BLACK)
        t_C = MathTex("C",color=BLACK).next_to(C,DOWN)
        D = Dot(cross_cl(c_B,l)[1],color=BLACK)
        t_D = MathTex("D",color=BLACK).next_to(D,LEFT)
        self.say(["以B为圆心、AB为半径",
                  "作圆B交圆A于另一点C",
                  "交给定直线于某一点D"],
                 Create(c_B),FadeIn(C,t_C,D,t_D))

        c_D = Circle(radius=distance(D,C),color=BLACK).move_to(D.get_center())
        E = Dot(cross_c(c_D,c_B)[0],color=BLACK)
        t_E = MathTex("E",color=BLACK).next_to(E,RIGHT)
        self.say(["以D为圆心、DC为半径",
                  "作圆D交圆B于另一点E"],
                 Create(c_D),FadeIn(E,t_E))

        AE = infinity_straight_line_cross_points(E,A,color=LEAF_RED)
        self.say(["过A、E作一条直线","我说，它与给定直线夹三分之二直角[=60°]"],
                 Create(AE))

        F = Dot(ex(cross_l(AE,l)),color=BLACK)
        t_F = MathTex("F",color=BLACK).next_to(F,RIGHT)
        self.say(["这是因为，设AE交给定直线于F"],
                 FadeIn(F,t_F))

        AB = Line(A.get_center(),B.get_center(),color=BLACK)
        BC = Line(B.get_center(),C.get_center(),color=BLACK)
        CA = Line(C.get_center(),A.get_center(),color=BLACK)
        ABCeq = VGroup(equal_line_notes(AB,size=0.5),equal_line_notes(BC,size=0.5),equal_line_notes(CA,size=0.5))
        self.say(["由于显然半径AB、BC、CA彼此相等",
                  "它们围成的三角形ABC是等边的",
                  "因此它的三个内角彼此相等[《几何原本》I.9]"],
                 *[Create(i)for i in [AB,BC,CA,ABCeq]])

        ABC = Polygon(A.get_center(), B.get_center(), C.get_center(), color=LEAF_RED,fill_opacity=0.37)
        self.say(["而三角形所有内角之和为两直角[I.32]",
                  "因此，它的每个内角都是三分之二直角"],
                 Create(ABC))

        DC = line_via_dot(D,C)
        DE = line_via_dot(D,E)
        DCeqDE = equal_lines_notes_group(DC,DE,n=2,size=0.5)
        self.say(["连接DC、DE",
                  "由于它们同是圆D的半径",
                  "它们相等"],
                 *[Create(i)for i in [DC,DE,DCeqDE]])

        BE = line_via_dot(B,E)
        BE1eq = equal_line_notes(BE,size=0.5)
        self.say(["连接BE，于是，它和BC同是圆B的半径",
                  "因此，BC等于BE"],
                 Create(BE),Create(BE1eq))

        BDC = polygon_via_dot(B,D,C,color=LIGHT_GRAY,fill_opacity=0.37)
        BDE = polygon_via_dot(B,D,E,color=LIGHT_GRAY,fill_opacity=0.37)
        self.say(["而BD边公用；",
                  "因此，在三角形BDC、BDE中，",
                  "角BDC等于角BDE."],
                 Create(BDC),Create(BDE))

        G = Dot(cross_cl(c_B,l)[0],color=BLACK)
        t_G = MathTex("G",color=BLACK).next_to(G,LEFT)
        EDC = polygon_via_dot(G, D, C, color=LIGHT_GRAY, fill_opacity=0.37)
        self.say(["设圆B交给定直线于另一点G，",
                  "则根据以前的推断，",
                  "角EDC等于角GDC的两倍."],FadeOut(BDC,BDE),
                 FadeIn(G,t_G),
                 Succession(Create(EDC),
                EDC.animate.become(polygon_via_dot(E,D,C,color=LEAF_YELLOW,fill_opacity=0.37))))
        self.play(FadeOut(EDC))

        GBC = polygon_via_dot(G, D, C, color=LIGHT_GRAY, fill_opacity=0.37)

        self.say(["但是，角GBC是与圆周角GDC对着同一个圆周的圆心角，",
                  "因此，角GBC也是角GDC的两倍；",
                  "因此，角GBC等于角GDC."],
                 Succession(Create(GBC),GBC.animate.become(polygon_via_dot(G,B,C,color=LEAF_YELLOW,fill_opacity=0.37))))
        self.play(FadeOut(GBC))

        CDE2CAE = polygon_via_dot(C,D,E,color=LEAF_YELLOW,fill_opacity=0.37)
        self.say(["但是，角CDE、CAE都是圆周CE所对的圆周角",
                  "因此它们相等."],
                 Succession(Create(CDE2CAE),CDE2CAE.animate.become(polygon_via_dot(C,A,E,color=LEAF_YELLOW,fill_opacity=0.37))))
        self.play(FadeOut(CDE2CAE))

        CAF2CBF = polygon_via_dot(C,A,F,color=LEAF_YELLOW,fill_opacity=0.37)
        self.say(["因此，角GBC等于角CAE",
                  "即角CAF等于角CBF"],
                 Succession(Create(CAF2CBF),
                            CAF2CBF.animate.become(polygon_via_dot(C,B,F,color=LEAF_YELLOW,fill_opacity=0.37))))
        self.play(FadeOut(CAF2CBF))

        c_ABC = DashedVMobject(circumcircle_of_triangle(A,B,C,color=LEAF_RED,fill_opacity=0))
        self.say(["因此，A、B、C、F四点共圆[III.27可证明的逆命题]"],
                  Create(c_ABC))

        self.say(["但是，在这个圆内，","角ACB、AFB都是圆周AB所对的圆周角","因此，角AFB等于角ACB"],
                 ABC.animate.become(Polygon(A.get_center(), B.get_center(), F.get_center(), color=LEAF_RED,fill_opacity=0.37)))
        self.say(["而角ACB是三分之二直角；","因此，角AFB也是三分之二直角，",
                  "而它是直线AE与给定直线夹成的角；",
                  "因此，这样作出来的直线AE与给定直线夹三分之二直角.",
                  "因此，这就是所要作的."])
        self.wait(6)
        self.play(FadeOut(c_ABC,ABC))

        DGC2DGE = polygon_via_dot(D,G,C,color=LEAF_YELLOW,fill_opacity=0.37)
        GC = line_via_dot(G,C)
        GE = line_via_dot(G,E)
        GCeqGE = equal_lines_notes_group(GC,GE,n=3,size=0.5)
        self.play(Create(DGC2DGE))
        self.say(["事实上，连接GC、GE.",
                 "由于DC等于DE，而DG公用，",
                  "且已经证明它们各自所夹的角GDC等于角GDE；",
                  "因此，在三角形DGC、DGE中，边GC等于边GE."],
                 Succession(Create(GC),Create(GE),DGC2DGE.animate.become(polygon_via_dot(D,G,E,color=LEAF_YELLOW,fill_opacity=0.37)),
                            Create(GCeqGE)))
        self.wait(3)
        self.play(FadeOut(DGC2DGE))

        c_G = DashedVMobject(Circle(radius=distance(G,E),color=LEAF_RED,fill_opacity=0)).move_to(G.get_center())
        self.say(["因此，如果在圆B与给定直线的另一个交点G上作第三个圆，","它会交圆B于同样的点，",
                  "也就是，依然可以用此方法作出所求直线."],Create(c_G),Indicate(E),Indicate(t_E))
        self.play(FadeOut(c_G,GE,GC,GCeqGE,DE,BE,DCeqDE[1],BE1eq,AE))

        CK = DC.copy()
        K = Dot(DC.copy().rotate(-60*DEGREES,about_point=C.get_center()).get_start(),color=BLACK)
        t_K = MathTex("K",color=BLACK).next_to(K,UP)
        KA = line_via_dot(K,A)
        DC2eq = equal_line_notes(DC.copy().rotate(-60*DEGREES,about_point=C.get_center()),2,size=0.5)
        self.say(["此外，向A所在的一侧作CK等于CD，","并使角KCD等于三分之二直角.","[I.3,I.23]","连接KA."],
                 Succession(Rotate(CK,-60*DEGREES,about_point=C.get_center()),FadeIn(K,t_K),Create(KA),Create(DC2eq)))

        BCDr2ACK = polygon_via_dot(B,C,D,color=LEAF_YELLOW,fill_opacity=0.37)
        ABC = polygon_via_dot(A,B,C,color=LEAF_RED,fill_opacity=0.37)
        self.say(["又，因为角ACB也是三分之二直角，",
                  "且CB等于CA；",
                  "三角形ACK实际上是由旋转三角形BCD得到的；",
                  "事实上，也不难证明它们全等[I.4]"],
                 Succession(Create(ABC),Create(BCDr2ACK)),is_wait=False)
        self.play(Rotate(BCDr2ACK,-60*DEGREES,about_point=C.get_center()))
        self.wait(6)
        self.play(FadeOut(BCDr2ACK,ABC))

        AK1eq = equal_line_notes(KA,1,size=0.5)
        BD1eq = equal_line_notes(line_via_dot(B,D),1,size=0.5)
        self.say(["因此，AK等于BD.",
                  "但BD等于AB，这是圆A、B公用的半径；",
                  "因此，K在圆A上."],
                 Create(AK1eq),Create(BD1eq)
                 )

        t = ["但是，连接KD，",
             "于是，三角形DCK是包含了一个三分之二直角的等腰三角形；",
             "因此，它也是等边三角形.[I.5,6,32可以推出]"]
        KD = line_via_dot(K,D)
        DCK = falling_maple(D,C,K)
        KD2eq = equal_line_notes(KD,2,size=0.5)
        self.say(t,Succession(Create(KD),Create(DCK),Create(KD2eq)))

        t=["因此，DC等于DK.",
           "因此，K在圆D上."
           "但是，它也在圆A上；",
           "因此，K是圆D和圆A的另一个交点."]
        self.say(t,Indicate(c_A),Indicate(c_D),Indicate(K),Indicate(t_K))

        t=["但是，已经证明，三角形ACK与三角形BCD是全等的；",
           "因此，角AKC等于角BDC；",
           "延长KA交给定直线于L；",
           "于是，角FKC等于角FDC."]
        BCDr2ACK = withered_leaf(B,C,D)
        L = F
        AL = line_via_dot(A,L)
        FKC2FDC = withered_leaf(F,K,C)

        self.say(t,is_wait=False)
        for i in [Create(BCDr2ACK), Rotate(BCDr2ACK, -60 * DEGREES, about_point=C.get_center()),
                   AnimationGroup(Create(AL),FadeOut(BCDr2ACK)),
                   Transform(t_F, MathTex("F(L)", color=BLACK).next_to(F, RIGHT)),
                   Create(FKC2FDC),
                   FKC2FDC.animate.become(withered_leaf(F, D, C)),FadeOut(FKC2FDC)]:
            self.play(i)

        t=["因此，C、F、K、D四点共圆[III.27可证明的逆命题]"]
        c_CFKD = DashedVMobject(circumcircle_of_triangle(C,F,K,color=LEAF_RED,fill_opacity=0))
        self.say(t,Create(c_CFKD))

        t=["因此，圆周KD所对的圆周角KFD、KCD相等；",
           "但是角KCD是三分之二直角，因为它是等边三角形KCD的一个内角；",
           "因此，直线KA与给定直线所夹的角KFD等于三分之二直角."]
        self.say(t,DCK.animate.become(falling_maple(D,F,K)))

        self.say(["因此，KA也是所求的直线",
                  "而K点正是圆D和圆A的另一个交点"],
                 Create(AE))

        self.say(["因此，KA和上一个方法作出的AE在同一条直线上；",
                  "因此，K、A、E、F、L都在同一条直线上，其中F和L根本就是一个点."],
                *[Indicate(i)for i in [K,A,E,F]])

        t=["此外，设圆A、B交于另一点M，",
           "而DK交圆B于N."]
        M = Dot(cross_c(c_B,c_A)[0],color=BLACK)
        t_M = MathTex("M(N)",color=BLACK).next_to(M,UL)
        N = M
        self.say(t,
                 FadeIn(M,t_M),FadeOut(DCK))

        t=["连接AM、BM，则显然三角形ABM等边；",
           "因此角MBA等于三分之二直角."]
        AM = line_via_dot(A,M)
        MB = line_via_dot(M,B)
        MBA = falling_maple(M,B,A)
        self.say(t,Succession(Create(AM),Create(MB),Create(MBA)))

        t=["连接BN；由于角CBN是以圆周角CDN所对的圆周CN为底的圆心角，",
           "因此它是后者的两倍；[III.20]",
           "而角CDN是三分之二直角，这是因为它是等边三角形KDC的一个内角；",
           "因此，角CBN等于三分之四直角."]
        KDC = falling_maple(K,D,C)
        self.say(t,Succession(Create(KDC),FadeOut(KDC)),is_wait=False)
        NDC2NBC2NBA = falling_maple(N,D,C)
        for i in [Create(NDC2NBC2NBA),NDC2NBC2NBA.animate.become(withered_leaf(N,B,C))]:
            self.play(i)
        self.wait(3)

        t=["但是角ABC等于三分之二直角；",
           "因此，余下的角NBA等于三分之二直角.",
           "因此，角NBA等于角MBA."]
        self.say(t,NDC2NBC2NBA.animate.become(falling_maple(N,B,A)))
        self.say(["而BN等于BM，且BA公用；",
                  "因此，AN等于AM；",
                  "因此，N也在圆A上；",
                  "因此，KD交圆A、B于同一点."],Indicate(M),Indicate(t_M))

        self.wait(3)
        self.play(FadeOut(NDC2NBC2NBA,MBA,c_CFKD),Transform(t_F,MathTex("F",color=BLACK).next_to(F,RIGHT)))

        t=["事实上，设圆A交给定直线于另一点于P.",
           "连接KP."]
        P = Dot(cross_cl(c_A,l)[0],color=BLACK)
        t_P = MathTex("P",color=BLACK).next_to(P,DR)
        KP = line_via_dot(K,P)
        self.say(t,
                 Succession(FadeIn(P,t_P),Create(KP)))#NeutronStar233

        t=["圆周CP所对的圆周角CKP、CBP相等.[III.27]"]
        CKP2CBP = withered_leaf(C,K,P)
        self.say(t,Succession(Create(CKP2CBP),CKP2CBP.animate.become(withered_leaf(C,B,P))))
        self.play(FadeOut(CKP2CBP))

        t=["但已经证明，角CBG等于角CDE."]
        CBG2CDE = withered_leaf(C,B,G)
        DE2eq= equal_line_notes(DE,2,size=0.5)
        self.say(t,FadeIn(DE,DE2eq),Create(CBG2CDE),CBG2CDE.animate.become(withered_leaf(C,D,E)),is_sequencing=True)

        CDE2CKE = CBG2CDE.copy()
        self.say(["且在圆D内，圆周CE所对的圆心角CDE等于两倍的圆周角CKE[III.20]"],
                 Create(CDE2CKE),CDE2CKE.animate.become(polygon_via_dot(C,K,E,color=LIGHT_GRAY,fill_opacity=0.37)),is_sequencing=True)

        self.say(["但已经证明，角CDE等于角CKP.","因此，角CKP等于二倍的角CKE.","事实上，三角形CDE、CKP全等，而这也是不难证明的."],
                 Rotate(CBG2CDE,-60*DEGREES,about_point=C.get_center()))

        CP = line_via_dot(C,P)
        CPpb = perpendicular_bisector_notes(CP,3)
        self.say(["因此，直线KAEF平分圆周CP.",
                  "因此，连接CP，",
                  "直线KAEF就是CP的垂直平分线.[III.26,III.3]"],
                 AnimationGroup(FadeOut(CDE2CKE,CBG2CDE),Create(CP)),Create(CPpb),is_sequencing=True)

        t=["因此，所求直线实际上可以由连接圆A和圆B、和给定直线的交点、",
           "并作出它的垂直平分线[I.10]得到."]
        self.say(t)

        to_fadeout = [i for i in self.mobjects if not i in {l,A,t_A}]
        self.play(FadeOut(*to_fadeout))
        self.play(FadeIn(A,t_A))
        self.saying = Text('')

        t=["现在使用直接作垂直平分线的方法，同样可以得证.",
           "像之前那样，作出圆A、圆B，设C是它们的一个交点，P是圆A与给定直线的另一个交点."]
        self.say(t,Create(c_A),FadeIn(B,t_B),Create(c_B),FadeIn(C,t_C,P,t_P),is_sequencing=True)

        self.say(["连接CP，作它的垂直平分线.","设它交给定直线于点F."],
                 Create(CP),AnimationGroup(Create(AE),Create(CPpb)),FadeIn(F,t_F),is_sequencing=True)

        t=["显然，由于C、P都是圆A上的点，CP的垂直平分线过圆心A；[参见III.1]",
           "且由于它是弦的垂直平分线，它平分圆周CP.",
           "连接AP、AC，设CP的垂直平分线在Q处平分较小的圆周CP."]
        Q = Dot(cross_cl(c_A,AE)[0],color=BLACK)
        t_Q = MathTex("Q",color=BLACK).next_to(Q,DR)
        AP = line_via_dot(A,P)
        AC = line_via_dot(A,C)
        self.say(t,FadeIn(Q,t_Q),Create(AC),Create(AP))
        self.wait(3)

        t=["于是，圆心角CAQ等于圆心角PAQ，,"
           "即等于一半的整个圆心角CAP."]
        CAQ = withered_leaf(C,A,Q)
        PAQ = CAQ.copy()
        self.say(t,Create(CAQ),Create(PAQ),PAQ.animate.become(withered_leaf(P,A,Q)),is_sequencing=True)

        t=["但是，圆周角CBP等于也等于一半的圆周角CAP，",
           "这是因为它们以相同的圆周CP为底[III.27]；",
           "因此，角CBP等于角CAQ."]
        self.say(t,PAQ.animate.become(withered_leaf(P,B,C)))
        self.play(FadeOut(CAQ,PAQ))

        t=["即，角CAF等于角CBF；",
           "因此，A、B、C、F四点共圆."]
        CAF2CBF = withered_leaf(C,A,F)
        c_ABCF = DashedVMobject(circumcircle_of_triangle(A,B,C,color=LEAF_RED))
        self.say(t,Create(CAF2CBF),CAF2CBF.animate.become(withered_leaf(C,B,F)),Create(c_ABCF),FadeOut(CAF2CBF),is_sequencing=True)

        t=["而三角形ABC显然等边；",
           "因此，它的内角ACB等于三分之二直角."]
        ABC = falling_maple(A,B,C)
        self.say(t,Create(ABC))

        t=["但是，已经证明，A、B、C、F四点共圆；",
           "因此，角AFB等于角ACB，",
           "也就等于三分之二直角."]
        self.say(t,ABC.animate.become(falling_maple(A,B,F)))

        t=["因此，所作的直线是过A点的、与给定直线夹三分之二直角的直线."]
        self.say(t)

        self.ending("这就是所要作的.")

class s2(Scene):
    def construct(self):
        t = right_aligned_text(["事实上，由于圆与圆、圆与直线之间，","多数情况下会产生两个交点,",
                                "而上述作法对于其中的任一一个都是成立的，"
                                "就像正在展示的那样.",
                                "还有，这个命题来自游戏Euclidea4.2."]).to_corner(UR)
        self.play(Write(t))
        self.wait(3.7)
class s3(Scene):
    def construct(self):
        t = right_aligned_text(["以及，在特殊的情况下，","最开始的方法中的交点E会与点A重合","容易证明，此时三角形CDE即三角形CDA，",
                                "是一个黄金三角形（底角是顶角的两倍的等腰三角形）.",
                                "但是，圆D与圆A的另一个交点则显然会一直存在，",
                                "因此，第一种作法之后的作法总是可以成立."])
        self.play(Write(t))
        self.wait(3.7)#NeutronStar233
