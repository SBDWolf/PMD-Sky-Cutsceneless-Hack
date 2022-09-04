
def 0 {
    sound_Stop();
    back2_SetMode(4);
    back2_SetGround(LEVEL_V01P03B);
    back_SetGround(LEVEL_D01P11B);
    supervision_Acting(0);
    Wait(1);
    camera2_SetPositionMark(Position<'m0', 33, 9.5>);
    with (performer 0) {
        camera_SetMyself();
    }
    supervision_SpecialActing(21, 600, 0);
    supervision2_SpecialActing(21, 600, 0);
    bgm_PlayFadeIn(BGM_EPILOGUE_THEME, 0, 256);
    screen2_FadeIn(0, 30);
    screen_FadeIn(1, 30);
    Wait(30);
    Wait(90);
    supervision_Acting(2);
    with (object OBJECT_D01P11B3_16) {
        SetupOutputAttributeAndAnimation(2, 0, 19);
    }
    with (object OBJECT_D01P11B3_16) {
        WaitAnimation();
    }
    Wait(30);
    Unlock(7);
    WaitExecuteObject(OBJECT_D01P11B3_16);
    with (object OBJECT_D01P11B3_16) {
        SetAnimation(1);
    }
    Wait(60);
    with (object OBJECT_D01P11B3_16) {
        SetOutputAttribute(1);
    }
    with (object OBJECT_D01P11B3_16) {
        SetAnimation(17);
    }
    with (object OBJECT_D01P11B3_16) {
        WaitAnimation();
    }
    WaitExecuteObject(OBJECT_D01P11B3_16);
    with (object OBJECT_D01P11B3_16) {
        SetAnimation(18);
    }
    with (object OBJECT_D01P11B3_16) {
        WaitAnimation();
    }
    supervision_Acting(1);
    with (actor ACTOR_PLAYER) {
        SetOutputAttribute(2);
    }
    with (actor ACTOR_PLAYER) {
        SetAnimation(2);
    }
    WaitExecuteObject(OBJECT_D01P11B3_16);
    with (object OBJECT_D01P11B3_16) {
        Destroy();
    }
    supervision_Acting(3);
    with (object OBJECT_D01P11B2_12) {
        SetOutputAttribute(2);
    }
    with (object OBJECT_D01P11B2_12) {
        SetOutputAttribute(1);
    }
    with (object OBJECT_D01P11B2_12) {
        SetAnimation(4);
    }
    Unlock(8);
    Wait(60);
    WaitLockLives(5, ACTOR_ATTENDANT1);
    Unlock(5);
    with (object OBJECT_D01P11B2_12) {
        SetAnimation(3);
    }
    Wait(70);
    with (object OBJECT_D01P11B2_12) {
        SetAnimation(2);
    }
    Wait(60);
    with (object OBJECT_D01P11B2_12) {
        SetAnimation(2);
    }
    Wait(30);
    with (object OBJECT_D01P11B2_12) {
        Destroy();
    }
    with (actor ACTOR_PLAYER) {
        Turn2Direction(8, 10, DIR_RIGHT);
    }
    Wait(60);
    WaitLockLives(6, ACTOR_ATTENDANT1);
    with (performer 0) {
        MovePositionMark(32896, Position<'m1', 40.5, 22.5>);
    }
    with (actor ACTOR_PLAYER) {
        Turn2Direction(8, 10, DIR_RIGHT);
    }
    with (actor ACTOR_ATTENDANT1) {
        MovePositionOffset(32844, -8, -8);
    }
    WaitExecuteLives(ACTOR_ATTENDANT1);
    with (actor ACTOR_ATTENDANT1) {
        Turn2Direction(4, 10, DIR_LEFT);
    }
    WaitExecuteLives(ACTOR_ATTENDANT1);
    WaitExecutePerformer(0);
    WaitBgmSignal();
    with (actor ACTOR_PLAYER) {
        MovePositionOffset(33152, 32, 0);
    }
    with (actor ACTOR_ATTENDANT1) {
        MovePositionOffset(33152, -36, 0);
    }
    WaitExecuteLives(ACTOR_PLAYER);
    WaitExecuteLives(ACTOR_ATTENDANT1);
    Wait(20);
    with (actor ACTOR_ATTENDANT1) {
        ExecuteCommon(CORO_JUMP_ANGRY_FUNC_SERIES, 0);
    }
    Wait(5);
    with (actor ACTOR_NPC_BIPPA) {
        SetEffect(EFFECT_LAUGHING, 3);
    }
    Wait(5);
    with (actor ACTOR_NPC_BIPPA) {
        ExecuteCommon(CORO_JUMP_HAPPY_FUNC_SERIES, 0);
    }
    WaitExecuteLives(ACTOR_ATTENDANT1);
    Wait(30);
    with (actor ACTOR_ATTENDANT1) {
        ExecuteCommon(CORO_JUMP_ANGRY_FUNC_SERIES, 0);
    }
    WaitExecuteLives(ACTOR_ATTENDANT1);
    Wait(45);
    with (actor ACTOR_ATTENDANT1) {
        SetAnimation(81);
    }
    with (actor ACTOR_ATTENDANT1) {
        WaitAnimation();
    }
    WaitExecuteLives(ACTOR_ATTENDANT1);
    Wait(30);
    screen2_FadeOut(0, 180);
    screen_FadeOut(1, 180);
    back2_SetMode(0);
    end;
}

def 1 for_actor(ACTOR_ATTENDANT1) {
    SetOutputAttribute(2);
    SetAnimation(81);
    WaitAnimation();
    Lock(5);
    SetAnimation(2);
    SetEffect(EFFECT_TWO_ARROWS_AT_SIDE_RIGHT, 3);
    WaitEffect();
    Wait(45);
    Turn2Direction(8, 1, DIR_LEFT);
    Wait(30);
    SetEffect(EFFECT_EXCLAMATION_MARK, 3);
    Lock(6);
    hold;
}

def 2 for_actor(ACTOR_NPC_BIPPA) {
    SetOutputAttribute(2);
    SetAnimation(2);
    SetOutputAttribute(1);
    SetPositionOffset(-2, 0);
    Lock(7);
    Wait(30);
    SetEffect(EFFECT_EXCLAMATION_MARK, 3);
    WaitEffect();
    Lock(8);
    CallCommon(CORO_JUMP_SURPRISE_FUNC);
    WaitEffect();
    Wait(45);
    CallCommon(CORO_JUMP_ANGRY_FUNC);
    Wait(15);
    CallCommon(CORO_JUMP_ANGRY_FUNC);
    hold;
}
